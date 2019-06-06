<template>
  
  <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid">
      <button type="button" id="sidebarCollapse" class="navbar-btn" 
      v-bind:class="{active: sidebar_collapse_flag}" v-on:click="got_clicked">
        <i class="far fa-arrow-alt-circle-left"></i>
        <span></span>
        <span></span>
        <span></span>
      </button>

      <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" 
      data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" 
      aria-label="Toggle navigation" v-on:click="topbar_flag = !topbar_flag">
        <i class="fas fa-align-justify"></i>
      </button>

      <div class="navbar-collapse" id="navbarSupportedContent" v-bind:class="{collapse: topbar_flag}">
        <ul class="nav navbar-nav ml-auto" style="float: right;">
          <li class="nav-item">
            <a class="nav-link" href="#">Com 1</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 2</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 3</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 4</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 5</a>
          </li>
          <li class="nav-item" v-on:click="run_the_software">
            <a class="nav-link" href="#">Run</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

</template>

<script>

import { EventBus } from '../main.js';
import { display_result } from '../vtkview.js';
export default {
  data : function() {
    return {
      topbar_flag : true,
      sidebar_collapse_flag : false,
      run_clicked_flag : false,
      input_param_obj : {},
      solver_result : {}
    };
  },
  methods : {
    got_clicked : function() {
      this.sidebar_collapse_flag = !this.sidebar_collapse_flag;
      EventBus.$emit('sidebar_flag_got_clicked', this.sidebar_collapse_flag);
    },
    run_clicked : function() {
      this.run_clicked_flag = true;
      this.input_param_obj = {};
      EventBus.$emit('run_got_clicked', this.run_clicked_flag);

      /*setTimeout(function() {
        EventBus.$on('inputParamFP_obj', (flat_panels_obj) => {
          Object.assign(this.input_param_obj, flat_panels_obj);
          console.log("hey");
        });
      },5000);*/
      
      /*EventBus.$on('inputParamFP_obj', (flat_panels_obj) => {
        Object.assign(this.input_param_obj, flat_panels_obj);
        console.log("hey");
      //});
      
      if (Object.keys(this.input_param_obj).length) {
        this.axios.post('/api/submit', this.input_param_obj).then(({data}) => {
        //this.data = data;
        });
      }
      });

      this.run_clicked_flag = false;*/
    
    },

    recieve_parameters : function() {
      EventBus.$on('inputParamPLANFORM_obj', (planform_input_obj) => {
        Object.assign(this.input_param_obj, planform_input_obj);
      });
      EventBus.$on('inputParamAI_obj', (advance_input_obj) => {
        Object.assign(this.input_param_obj, advance_input_obj);
      });
      EventBus.$on('inputParamFP_obj', (flat_panels_obj) => {
        Object.assign(this.input_param_obj, flat_panels_obj);
      });
      EventBus.$on('inputParamVOLUTE_obj', (volute_obj) => {
        Object.assign(this.input_param_obj, volute_obj);
      });
      EventBus.$on('inputParamBL_obj', (brake_lines_obj) => {
        Object.assign(this.input_param_obj, brake_lines_obj);
      });
      EventBus.$on('inputParamRLA_obj', (rla_obj) => {
        Object.assign(this.input_param_obj, rla_obj);
      });
      EventBus.$on('inputParamAI_obj', (advance_input_obj) => {
        Object.assign(this.input_param_obj, advance_input_obj);
      });

      /*this.input_param_obj["mesh_parameters"] = {
        "fixed_node_file_name": "../solverMain/test/fixed_nodes.txt", 
        "edge_length_percentc": 3.0, 
        "mesh_file_name": "../solverMain/test/cad_surfacefile.vtk", 
        "geometry_file_name": "../solverMain/test/gmsh_file.geo"
      }*/
    },

    create_request : function() {
      this.axios.post('/api/submit', this.input_param_obj).then((res) => {
        Object.assign(this.solver_result, res.data);
        console.log(res.data);
        if (this.solver_result["runcode"] == 0) {
          display_result();
        }
        EventBus.$emit("solver_overall_result", this.solver_result);
      }).catch(error => {
        console.log(error);
      });
    },

    run_the_software : function() {
      this.run_clicked();
      this.recieve_parameters();
      this.run_clicked();
      this.recieve_parameters();
      this.create_request();
    }

  },
}
</script>
