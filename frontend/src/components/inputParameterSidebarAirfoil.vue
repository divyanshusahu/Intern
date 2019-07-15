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
              <p>Chord length <span class="d-none d-sm-inline-block">percentage</span></p>
            </div>
            <div class="col">
              <input type="number" value="5.0" name="airfoil_clp" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Angle with chord length</p>
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
            <div class="row">
              <div class="col">
                <p>Or from file</p>
              </div>
              <div class="col">
                <input type="file" accept=".txt" id="user_defined_input" />
              </div>
            </div>
            <div id="airfoil_plot" class="d-none d-md-block">
              
            </div>
          </fieldset>
        </div>
      </div>
      <div class="card-footer">
        <button type="button" class="btn btn-success" v-on:click="input_toggle = !input_toggle">Apply</button>
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
  }
}
</script>

