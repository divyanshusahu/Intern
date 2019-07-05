from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import json
from cloud_connect import create_presigned_url
import snowflake
import boto3
import settings
from case_model import CaseModel

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/submit", methods=['POST'])
def submit_job() :
  data = request.get_json()
  data["mesh_parameters"] = {
    "fixed_node_file_name" : "/work/fixed_nodes.txt",
    "mesh_file_name" : "/work/cad_surfacefile.vtk",
    "geometry_file_name" : "/work/gmsh_file.geo"
  }
  solver_run_status_code = 0

  snowflake_generator = snowflake.generator(1,1)
  case_id = next(snowflake_generator)

  upload_to_s3_path = "%s/input.scf" % (case_id)
  upload_file = boto3.resource('s3')
  upload_file_object = upload_file.Object(settings.BUCKET_NAME, upload_to_s3_path)
  upload_file_object.put(
    Body=(bytes(json.dumps(data).encode('UTF-8')))
  )

  batch = boto3.client('batch')
  result = batch.submit_job(jobName='Paraview_%s' % (case_id),
                jobQueue=settings.JOB_QUEUE,
                jobDefinition=settings.JOB_DEFINITION,
                parameters={
                  'input_path' : '%s/input.scf' % (case_id)
                },
                containerOverrides={
                  'environment': [
                    {
                      'name': 'BUCKET_NAME',
                      'value': settings.BUCKET_NAME
                    },
                    {
                      'name': 'AWS_REGION',
                      'value': settings.AWS_REGION
                    }
                  ]
                },
                retryStrategy={
                  'attempts':1
                },
                timeout={
                  'attemptDurationSeconds': 86400*30
                })
  job_id = result['jobId']

  if not CaseModel.exists() :
    CaseModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
  case = CaseModel(str(case_id), str(job_id))
  case.save()

  return_output = {'case_id' : str(case_id)}
  return jsonify(return_output)

@app.route('/api/job_status', methods=['POST'])
def check_job_status() :
  data = request.get_json()
  batch = boto3.client('batch')
  try :
    for case in CaseModel.query(data['case_id']) :
      job_id = case.attribute_values['job_id']
  except Exception as e:
    print(e)
    return jsonify(runcode=10)
  
  response = batch.describe_jobs(
    jobs=[
      job_id
    ]
  )
  
  url = None
  if response['jobs'][0]['status'] == 'SUCCEEDED' :
    filename = "%s/cad_surfacefile.vtp" % (data['case_id'])
    url = create_presigned_url(filename)
  
  return jsonify(url=url, current_status=response['jobs'][0]['status'])

@app.route('/api/download_dxf', methods=['POST'])
def download_dxf() :
  data = request.get_json()
  case_id = data["case_id"]
  download_dxf_name = "%s/drawing.dxf" % (case_id)
  download_dxf_url = create_presigned_url(download_dxf_name)

  return jsonify(url=download_dxf_url)

if __name__ == '__main__':
  app.run(debug=True)
