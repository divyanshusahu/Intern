from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import json, subprocess
import os
from cloud_connect import create_presigned_url
import snowflake
import boto3
import sqlite3
import settings
from case_model import CaseModel
"""from flask_restful import Resource, Api"""

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#api = Api(app)

"""class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')"""

@app.route("/api/submit", methods=['POST'])
def submit_job() :
    data = request.get_json()
    data["mesh_parameters"] = {
        "fixed_node_file_element" : "/work/fixed_nodes.txt",
        "edge_length_percentc" : 3,
        "mesh_file_name" : "/work/cad_surfacefile.vtk",
        "geometry_file_name" : "/work/gmsh_file.geo"
    }
    solver_run_status_code = 0
    """result = {}
    global current_status
    with open('./tmp/input.scf', 'w') as f :
        try :
            json.dump(data, f)
            result['input_file'] = "Input Parameters Processing"
            current_status = "Input Parameters Processing"
        except :
            result['input_file'] = "Input Failed"
            current_status = "Input Failed"
            os._exit(0)
    
    result['input_file_result'] = "Processing Complete"
    current_status = "Processing Complete"

    try :
        c1 = "../solverMain/solverMain tmp/input.scf"
        r1 = subprocess.run(c1, shell=True).returncode
        if r1 == 0 :
            result['running_solver'] = "Running the Solver"
            current_status = "Running the Solver"
        else :
            result['running_solver'] = "Solver Failed"
            current_status = "Solver Failed"
    except :
        os._exit(0)
    
    result['running_solver_result'] = "Solver Successful"
    current_status = "Solver Successful"

    try :
        c2 = "cp ../solverMain/test/gmsh_file.geo tmp/"
        subprocess.run(c2, shell=True)
        c3 = "gmsh tmp/gmsh_file.geo -algo del2d -2 -bin -o tmp/cad_surfacefile.vtk"
        r3 = subprocess.run(c3, shell=True).returncode
        if r3 == 0 :
            result['running_gmsh'] = "Running gmsh"
            current_status = "Running gmsh"
        else :
            result['running_gmsh'] = "gmsh failed"
            current_status = "gmsh failed"
    except :
        os._exit(0)

    result['running_gmsh_result'] = "gmsh successful"
    current_status = "gmsh successful"

    try :
        c4 = "../vtk_to_vtp/vtkunstructured_to_polydataset tmp/cad_surfacefile.vtk tmp/cad_surfacefile.vtp"
        r4 = subprocess.run(c4, shell=True).returncode
        if r4 == 0 :
            result['converting_vtp'] = "Converting to vtp"
            current_status = "Converting to vtp"
        else :
            result['converting_vtp'] = "Conversion to vtp failed"
            current_status = "Conversion to vtp failed"
    except :
        os._exit(0)
    
    result['converting_vtp_result'] = "converted to vtp"
    current_status = "converted to vtp"

    return jsonify( input_file = result['input_file'],
                    input_file_result = result['input_file_result'],
                    running_solver = result['running_solver'],
                    running_solver_result = result['running_solver_result'],
                    running_gmsh = result['running_gmsh'],
                    running_gmsh_result = result['running_gmsh_result'],
                    converting_vtp = result['converting_vtp'],
                    converting_vtp_result = result['converting_vtp_result'],
                    success="OK")"""

    snowflake_generator = snowflake.generator(1,1)
    case_id = next(snowflake_generator)
    
    """input_file_path = "./tmp/input.scf"
    with open(input_file_path, 'w') as f :
        try :
            json.dump(data, f)
        except :
            solver_run_status_code = 1
            return jsonify(runcode=solver_run_status_code)
        
    upload_to_s3_path = "%s/input.scf" % (case_id)
    try :
        upld_fl(input_file_path, upload_to_s3_path)
    except :
        solver_run_status_code = 1
        return jsonify(runcode=solver_run_status_code)"""

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

    """connection = sqlite3.connect('pp103.db')
    c = connection.cursor()
    db_insert_data = [case_id, job_id]
    c.execute("INSERT INTO cases VALUES (?,?)", db_insert_data) 
    c.commit()
    c.close()

    try :
        with connection :
            db_insert_data = [case_id, job_id]
            connection.execute("INSERT INTO cases VALUES (?,?)", db_insert_data)
    except :
        solver_run_status_code = 1
        return jsonify(runcode=solver_run_status_code)"""

    if not CaseModel.exists() :
        CaseModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    case = CaseModel(str(case_id), str(job_id))
    case.save()

    #solver_run_status_code = run_solver(input_file_path)

    #solver_run_status_code = subprocess.run("python3 run_process.py ./tmp/input.scf", shell=True).returncode
    #cwd = os.getcwd()
    #tmp_folder = os.path.join(cwd, 'tmp')
    #docker_command = "docker run paraview python3.6 /python/run_process.py %s" % (upload_to_s3_path)
    #solver_run_status_code = subprocess.Popen(docker_command, shell=True).returncode
    #proc = subprocess.run(docker_command, shell=True, stdout=subprocess.PIPE)
    #return_output = str(proc.stdout).split('\\n')
    #return_output = return_output[-2]
    #return_output = json.dumps(return_output)
    #return_output = json.loads(return_output)
    #return return_output
    return_output = {'case_id' : str(case_id)}
    return jsonify(return_output)

'''@app.route("/tmp/cad_surfacefile.vtp", methods=['GET'])  # Now hardcoded change accordingly
@cross_origin()  
def show_output():
    return send_from_directory("tmp", "cad_surfacefile.vtp")'''


@app.route('/api/job_status', methods=['POST'])
def check_job_status() :
    data = request.get_json()
    batch = boto3.client('batch')
    #conn = sqlite3.connect('pp103.db')
    #c = conn.cursor()
    try :
        """c.execute("SELECT * FROM cases WHERE case_id=?", [int(data['case_id']),])
        result = c.fetchall()
        c.close()
        case_id, job_id = result[0]"""
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


if __name__ == '__main__':
    app.run(debug=True)
