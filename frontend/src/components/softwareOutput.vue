<template>
  <div id="output_screen">
    <div id="view_toolbar">
      <ul class="tabs_3d_2d">
        <li v-bind:class="{toolbar_active:drawing_3d_flag}" v-on:click="drawing_3d_flag=true">3D</li>
        <li v-bind:class="{toolbar_active:!drawing_3d_flag}" v-on:click="drawing_3d_flag=false">2D</li>
      </ul>
      <ul class="view_icons" v-if="drawing_3d_flag">
        <li v-on:click="change_view('front')">
          <img src="../assets/views/frontview.png" alt="Front View" title="Front View">
        </li>
        <li v-on:click="change_view('back')">
          <img src="../assets/views/backview.png" alt="Back View" title="Back View">
        </li>
        <li v-on:click="change_view('left')">
          <img src="../assets/views/leftview.png" alt="Left View" title="Left View">
        </li>
        <li v-on:click="change_view('right')">
          <img src="../assets/views/rightview.png" alt="Right View" title="Right View">
        </li>
        <li v-on:click="change_view('top')">
          <img src="../assets/views/topview.png" alt="Top View" title="Top View">
        </li>
        <li v-on:click="change_view('bottom')">
          <img src="../assets/views/bottomview.png" alt="Bottom View" title="Bottom View">
        </li>
      </ul>
    </div>
    <div id="softwareOutput" class="card" v-bind:class="{display_none_element:!drawing_3d_flag}">
      <!--<img class="card-img-top" src="../assets/images/p1.jpg">-->
      <div class="content"></div>
      <div id="loader">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
        <div class="bar4"></div>
        <div class="bar5"></div>
        <div class="bar6"></div>
      </div>
    </div>
    <div id="dxf_output" v-if="!drawing_3d_flag">
      <button class="btn btn-success" v-on:click="download_dxf">Download DXF</button>
    </div>
  </div>
</template>

<script>
import { EventBus } from "../main.js";
import { saveAs } from "file-saver";
import { change_camera_view } from "../vtkview.js";
export default {
  data: function() {
    return {
      drawing_3d_flag: true,
      caseID: {}
    };
  },
  created() {
    EventBus.$on("dxf", (caseID) =>{
      this.caseID = caseID;
    });
  },
  methods: {
    download_dxf : function() {
      if (this.caseID.hasOwnProperty('case_id')) {
        console.log(this.caseID);
        this.axios.post("/api/download_dxf", this.caseID).then((res) => {
          saveAs(res.data["url"], "ram_2d_drawing.dxf");
        })
      }
    },
    change_view : function(view) {
      change_camera_view(view);
    }
  }
};
</script>