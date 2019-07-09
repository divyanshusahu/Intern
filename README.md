# Ram ParaZ

## Documentation

### Front End

Frontend is build using VueJS 2.

#### Get Started

```bash
cd frontend
npm install
npm run serve
```

The basics of VueJS can be found [here](https://vuejs.org/v2/guide/).

**Page Structure**

```html
<!-- page structure -->

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

**Dependencies**

1. *bootstrap-vue* is used for styling.
2. *vue-axios* is used for creating the requests.
3. *vue2-touch-events* is used for adding swipe functionality on sidebar.
4. Event Bus is used for transfering variables from one components to another.

**Components**

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

- fileSidebar (fileSidebar.vue, save_inputs.js, vtkview.js)
File menu has four list elements. Function 'initLocalFileLoader' is used from vtkview.js
New (For clearing the output screen)
Open (For displaying the pre generated vtp file on the screen)
Save Project (For saving the current input json locally)
Load Project (For loading the inputs from the file)

- viewSidebar (viewSidebar.vue, vtkview.js)
View Sidebar has six list elements named 'front view', back view', left view', right view', top view', bottom view'.
After adding the view icons in the toolbar viewSide is not included in rendering.
Function 'change_camera_view' is used from vtkview.js

- inputParameterSidebar (inputParameterSidebar.vue)
It has seven different parameters list elements.

- roundCanopySidebar (roundCanopySidebar.vue)
It contain round canopy input parameters.

- solverSidebar (solverSidebar.vue)
It contains two list elements named 'Stop Solver'  and 'Run Solver'.

- helpSidebar (helpSidebar.vue)
It contains two list elements named 'help' and 'manual'. 

**Topbar (topbar.vue, topbar.css)**

It has Sidebar toggle button with inputs parameter icons with a Run botton.

**Software Output (softwareOutput.vue, softwareOutput.css)**

The toolbar has two tabs for 3D and 2D display followed by six different view icons.
The renderer screen first display a loader than followed by output canvas.

**Output Log (outputLog.vue, outputLog.css)**

**All Inputs Popup (allInputs.vue)**

### Backend

Python Flask framework is used for backend.

```bash
cd backend
pip install -r requirments.txt
flask run
```

1. First we create a post request at **/api/submit**. 
2. It then upload the input.scf project file to S3 Bucket. 
3. Then it submit the AWS Fargate task.
4. The case_id, task_id pair is saved in dynamo db.
5. It returned the job_id.
6. Then again we create a post request at **/api/job_status** with case_id as a data.
7. It then checks for the output file created in the S3 bucket. If created then return the pre_signed url else return null.
8. There is another route **/api/download_dxf** to download the output dxf file.

### Docker Image

1. The Docker image is based on Ubuntu 18.04
2. The image first download the uploaded input.scf from S3 Bucket.
3. It then run the solver and upload the output vtp and dxf file back to S3 bucket.

### AWS Fargate

Our used confriguation: 0.5 vCPU, 1GB memory

Each vCPU is a thread of a CPU core, except for T2 instances.

Price: 
$0.04256 per hour per vCPU
$0.004655 per hour per GB memory

Pricing is per second with a 1-minute minimum. Duration is calculated from the time you start to download your container image (docker pull) until the Task terminates, rounded up to the nearest second.

Our task is completed around 40 to 50 seconds.

**Estimated Cost per Execution**
cost = (0.04256*0.5)/60 + (0.004655)/60
cost = 0.000355 + 0.0000775
cost = **$0.0004325** 
cost = **0.03**