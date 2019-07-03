<template>
  <div class="custom_modal" id="round_canopy_modal" v-bind:class="{pop_up_toggle: input_toggle}">
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Round Parachute
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <fieldset>
            <legend>
              <input type="checkbox" v-model="round_canopy_checkbox" />
            </legend>
            <div v-bind:class="{disabledDiv:!round_canopy_checkbox}">
              <fieldset>
                <legend>Round Parachute</legend>
                <div class="row">
                  <div class="col">
                    <p>No of Panels</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="20"
                      name="round_canopy_n_panels"
                      style="width:100px;"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>No of Suspension Lines</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="9"
                      name="round_canopy_n_susplines"
                      style="width:100px;"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>No of Slots</p>
                  </div>
                  <div class="col">
                    <input type="number" value="6" name="round_canopy_n_slot" style="width:100px;" />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>External Diameter</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="10000"
                      name="round_canopy_exdia"
                      style="width:100px;"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Ring Diameter</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="1000"
                      name="round_canopy_ringdia"
                      style="width:100px;"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Slot width</p>
                  </div>
                  <div class="col">
                    <input type="number" value="100" name="round_canopy_sw" style="width:100px;" />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Suspension Length</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="1000"
                      name="round_canopy_susplen"
                      style="width:100px;"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Conical Height</p>
                  </div>
                  <div class="col">
                    <input type="number" value="0" name="round_canopy_conhg" style="width:100px;" />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Skirt Width</p>
                  </div>
                  <div class="col">
                    <input type="number" value="0" name="round_canopy_skwdt" style="width:100px;" />
                  </div>
                </div>
              </fieldset>
              <br />
              <fieldset>
                <legend>Sewing Allowance</legend>
                <div class="row">
                  <div class="col">
                    <p>Max Value (mm)</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="50.0"
                      name="rc_sa_max_value"
                      style="width: 100px"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Min Value (mm)</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="1.0"
                      name="rc_sa_min_value"
                      style="width: 100px"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Panel Sides (% of chord)</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="0.5"
                      name="rc_panels_sap_sides"
                      style="width: 100px"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Panel Front (% of chord)</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="0.5"
                      name="rc_panels_sap_front"
                      style="width: 100px"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">
                    <p>Panel Rear (% of chord)</p>
                  </div>
                  <div class="col">
                    <input
                      type="number"
                      value="0.5"
                      name="rc_panels_sap_rear"
                      style="width: 100px"
                    />
                  </div>
                </div>
              </fieldset>
            </div>
          </fieldset>
        </div>
      </div>
      <div class="card-footer">
        <button
          type="button"
          class="btn btn-success"
          v-on:click="input_toggle = !input_toggle"
        >Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import { EventBus } from "../main.js";
export default {
  data: function() {
    return {
      input_toggle: true,
      round_canopy_checkbox: false
    };
  },
  created() {
    EventBus.$on("rc_input_param_got_clicked", rc_input_param_flag => {
      this.input_toggle = rc_input_param_flag;
    });
  }
};
</script>