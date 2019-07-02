<template>
  
  <div class="custom_modal" id="airfoil_modal"
  v-bind:class="{pop_up_toggle : input_toggle}">
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>Airfoil Input<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <div class="row">
            <div class="col">
              <span>Chord length percentage</span>
            </div>
            <div class="col">
              <input type="number" value="5.0" name="airfoil_clp" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <span>Angle with chord length</span>
            </div>
            <div class="col">
              <input type="number" value="135.0" name="airfoil_acl" style="width: 100px">
            </div>
          </div>
          <fieldset>
            <legend>Airfoil</legend>
            <div class="row">
              <div class="col">
                <p>Standard Airfoil</p>
              </div>
              <div class="col">
                <select name="standard_airfoil" v-model="std_airfoil">
                  <option value="ClarkY">ClarkY</option>
                  <option value="NACA 0012">NACA 0012</option>
                  <option value="NACA 0009">NACA 0009</option>
                </select>
              </div>
            </div>
            <div id="airfoil_plot" class="d-none d-md-block">
              
            </div>
          </fieldset>
        </div>
      </div>
      <div class="card-footer">
        <button type="button" class="btn btn-success" v-on:click="input_toggle = !input_toggle">Close</button>
      </div>
    </div>
  </div>

</template>

<script>
import { EventBus } from '../main.js';
import { airfoil_plot } from '../plotly_airfoil.js';
export default {
  data : function() {
    return {
      input_toggle : true,
      airfoil_input_obj : {},
      std_airfoil: 'ClarkY'
    }
  },
  mounted : function() {
    airfoil_plot(this.std_airfoil);
  },
  watch : {
    std_airfoil : function() {
      airfoil_plot(this.std_airfoil);
    }
  },
  created() {
    EventBus.$on('input_param_airfoil_got_clicked', (input_param_airfoil_flag) => {
      this.input_toggle = input_param_airfoil_flag;
    });

    EventBus.$on('run_got_clicked', (run_clicked_flag) => {
      if (run_clicked_flag)
      {
        this.airfoil_input_obj["rib_description"] = {
          "LE_cut" : {
            "angle_with_chord_line" : parseFloat(document.getElementsByName("airfoil_acl")[0].value),
            "chord_length_percentc" : parseFloat(document.getElementsByName("airfoil_clp")[0].value)
          },
          "lightening_holes": [
            {
              "shape": "ELLIPTIC", 
              "box_index": 0, 
              "minor_to_major_axes": 0.7, 
              "size": 5
            }, 
            {
              "shape": "TRIANGULAR", 
              "box_index": 1, 
              "minor_to_major_axes": 0.7
            }
          ],
          "aerofoil" : "/solverMain/test/airfoil.txt",
          "tape_V_angle":20
        };
        EventBus.$emit('inputParamAI_obj', this.airfoil_input_obj);
      }
    });
  }
}
</script>

