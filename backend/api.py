from flask import Flask, request, jsonify, send_from_directory
"""from flask_restful import Resource, Api"""

app = Flask(__name__)
#api = Api(app)

"""class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')"""

@app.route("/api/submit", methods=['POST'])
def submit_job() :
    data = request.get_json()
    result = {}
    with open('./tmp/input.scf', 'w') as f :
        try :
            f.write(str(data))
            result['input_file'] = "Input Parameters Processing"
        except :
            result['input_file'] = "Input Failed"
    #print(jsonify(input_file = result['input_file']))
    return jsonify( input_file = result['input_file'],
                    success="OK")

@app.route("/tmp/test.vtp", methods=['GET']) # Now hardcoded change accordingly
def show_output() :
    return send_from_directory("tmp", "test.vtp")


if __name__ == '__main__':
    app.run(debug=True)
    
