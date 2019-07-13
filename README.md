# Ram ParaZ

## Documentation

### Front End

The frontend is build using VueJS 2.

#### Get Started

```bash
cd frontend
npm install
npm run serve
```

The basics of VueJS can be found [here](https://vuejs.org/v2/guide/).

**Dependencies**

1. *bootstrap-vue* is used for styling.
2. *vue-axios* is used for creating the requests.
3. *vue2-touch-events* is used for adding swipe functionality on the sidebar.
4. Event Bus is used for transferring variables from one component to another.

**Directory Structure**

```bash
public
src
babel.config.js
package-lock.json
package.json
vue.config.json
```

1. *vue.config.js* : This file contains user define configuration for the vue development environment.

**Directory Structure (public)**

```bash
public\
  index.html
  favicon.png
```

**Page Structure**

```html
<!-- page structure -->
<!-- index.html -->

<div id="app">
  <div class="wrapper">
	<sidebar />
	<div id="content">
	  <topbar />
	  <softwareOutput />
	  <outputLog />
	</div>
  </div>
	
  <!-- Input Pop-up divs -->
  <allInputs />
</div>
```

**Directory Structure (src)**

```bash
src/
  assets/
  components/
  App.vue
  dxf_viewer.js
  main.js
  plotly_airfoil.js
  save_inputs.js
  vtkview.js
```

1. *dxf_viewer.js* : This file use *'viewerjs'* library to display the output DXF in image format(png, jpg, jpeg)
2. *plotly_airfoil.js* : This file use *'plotly.js'* library to plot the airfoil graph.
3. *save_inputs.js* : This file contains four functions.
	1. collect_inputs() : This function collects all the input parameters from the HTML page and saves it as a JSON object.
	2. save_input() : This function uses *'file-saver'* library to save the inputs in a file.
	3. merge_inputs() : This function is used to load an input file from the local computer and update the inputs values in the HTML page.
	4. load_input() : This function is used to read the JSON file uploaded by the user.
4. *vtk_view.js* : This file contains the code of VTK geometric viewer. Three user-defined functions are created at the end of the file.
	1. initLocalFileLoader() : This function is used to read and load the local VTP file to the renderer screen.
	2. display_result() : This function is used to read and load the VTP file from the URL and display it in the renderer screen.
	3. change_camera_view() : This function is used to change the camera view.
5. *main.js* : This file contains all the configurations for the app page. All the modules should be imported in this file to used it on all the components.
6. *App.vue* : This page defines the page structure of index.html stated above. All the CSS files should be imported here.

#### Components

**Sidebar (sidebar.vue, sidebar.css)**

```html
<!-- sidebar structure -->
<nav id="sidebar">
  <ul>
	<fileSidebar />
	<!-- viewSidebar -->
	<inputParameterSidebar />
	<roundCanopySidebar />
	<solverSidebar />
	<helpSidebar />
  </ul>
</nav>
```

* _fileSidebar (fileSidebar.vue, save_inputs.js, vtkview.js)_
	* File menu has four list elements. Function 'initLocalFileLoader' is used from vtkview.js
	* Open (For displaying the pre-generated VTP file on the screen)
	* Save Project (For saving the current input JSON locally)
	* Load Project (For loading the inputs from the file)

* _viewSidebar (viewSidebar.vue, vtkview.js)_
	* View Sidebar has six list elements named 'front view', back view', left view', right view', top view', bottom view'.
	* After adding the view icons in the toolbar viewSide is not included in rendering.
	* Function 'change_camera_view' is used from vtkview.js

* _inputParameterSidebar (inputParameterSidebar.vue, save_inputs.js)_
	* It has seven different input parameters list elements.

* _roundCanopySidebar (roundCanopySidebar.vue, save_inputs.js)_
	 * It contains round canopy input parameters.

* solverSidebar (solverSidebar.vue)
	* It contains two list elements named 'Stop Solver'  and 'Run Solver'.

* helpSidebar (helpSidebar.vue)
	* It contains two list elements named 'help' and 'manual'. 

**Topbar (topbar.vue, topbar.css, save_inputs.js)**

* It has Sidebar toggle button with inputs parameter icons with a Run button.

**Software Output (softwareOutput.vue, softwareOutput.css)**

* This div is diveded into two parts toolbar and output display.
* The toolbar has two tabs for 3D and 2D display followed by six different view icons.
* The 3D display initially have a dummy image. After clicking 'Run' it is replaced with a loader. When the output is ready the loader is replaced by the output canvas.
* The 2D display shows the converted jpeg or png image of the dxf with a download dxf button.

**Output Log (outputLog.vue, outputLog.css, vtkview.js)**

* This component send a request to the server in every five seconds to check the status of the output files. If the server return 'succeeded' it clears the interval and call the display_result() function from _vtkview.js_.

**All Inputs Popup (allInputs.vue, customModal.css)**

```html
<!-- This div is hidden by default -->
  <div>
    <roundCanopyInput />
    <inputParameterSidebarPlanform />
    <inputParameterSidebarAirfoil />
    <inputParameterSidebarVolute />
    <inputParameterSidebarAl />
    <inputParameterSidebarFp />
    <inputParameterSidebarRLA />
    <inputParameterSidebarBL />
    <inputParameterSidebarAi />
  </div>
```

This div is hidden by default. On clicking the input parameters button it toggles the display flag and the respective input modal is shown.

----

### Backend

#### Getting Started

Python3 and Python Flask framework is used for backend.

```bash
cd backend
pip install -r requirments.txt
flask run
```

**Directory Structure**

```bash
.flaskenv
api.py
case_model.py
cloud_connect.py
requirments.txt
run_process.py
settings.py
snowflake.py
```

**Files Description**

1. .flaskenv (contains flask configuration environment variables)
2. api.py : flask app (contains different routes)
	1. */api/submit* : We submit the input json through post request at this route. It collects the input data and uploaded it in S3 bucket as filename *'case_id/input.scf'*. After uploading the file it initiate ecs run task function which is used to invoke fargate instance. Then it save the case_id and task_id pair in dynamoDB. This route return the case_id.
	2. */api/job_status* : It checks if the output file is generated or not. It takes case_id as an input and checks for *"case_id/cad_surfacefile.vtp"* in S3 bucket. It uses a boto3 object to check if the output file is present or not. If present then return 'SUCCEEDED' else return 'RUNNING'.
	3. */api/download_dxf* : This route is used to download the generated dxf file. It takes case_id as an input and search for dxf file in S3 bucket *"case_id/drawing.dxf"*. Then it generate a pre_signed url for it to download.
3. case_model.py : This file contains the code for dymanoDB. The case_id, task_id pair is saved using in the table name case. Python library pynamodb is used for this operations.
4. *cloud_connect.py* : This files contains three boto3 functions to upload, download and create presigned url functions.
5. *requirments.txt* : This files contains all the dependencies for backend environment.
6. *run_process.py* : This files contains the system call commands to run the solver. We copy this file inside the docker image. It first run the respective solver(solverMain or roundCanopy) then it runs gmsh followed by vtk_to_vtp. The output files are uploaded back to S3 bucket using function created in *cloud_connect.py*.
7. *settings.py* : This file contains the environment variables.
8. *snowflake.py* : This file contain the code for generating the case_id.

----

### Docker Image (Dockerfile)

1. The Docker image is based on Ubuntu 18.04
2. The python code is in /python/ directory.
3. The solver code is inside /solverMain/ directory.
4. The output generated files are saved in /work/ folder.
5. The image first download the uploaded *input.scf* from S3 Bucket using a function upld_file written in *cloud_connect.py*.
6. It then run the solver from file *run_process.py* and upload the output vtp and dxf file back to S3 bucket using *cloud_connect.py*.

----

### AWS Services

#### S3 Bucket

* S3 bucket is used to save the input.scf and the generated output vtp and dxf files.

#### ECR

* ECR is used to store our docker image in aws repository.

#### ECS

* ECS is used to create a cluster which is used to define the Fargate confriguations and environment.

#### Fargate

Our used confriguation: 0.5 vCPU, 1GB memory

Each vCPU is a thread of a CPU core, except for T2 instances.

Price: 
$0.04256 per hour per vCPU

$0.004655 per hour per GB memory

Pricing is per second with a 1-minute minimum. Duration is calculated from the time you start to download your container image (docker pull) until the Task terminates, rounded up to the nearest second.

Our task is completed around 40 to 50 seconds.

**Estimated Cost per Execution**

```python
cost = (0.04256*0.5)/60 + (0.004655)/60
cost = 0.000355 + 0.0000775
cost = 0.0004325 dollars 
cost = 0.03 Rs
```