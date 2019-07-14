<template>
  <div class="custom_modal" id="advance_input_modal" v-bind:class="{pop_up_toggle : input_toggle}">
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Advance Input
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <fieldset>
            <legend>Washout Description</legend>
            <div class="row">
              <div class="col">
                <span>Tip angle <span class="d-none d-sm-inline-block">(deg)</span></span>
              </div>
              <div class="col">
                <input
                  type="number"
                  value="0.0"
                  name="advip_washout_description_ta"
                  style="width: 100px"
                />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Center of Rotation</span>
              </div>
              <div class="col">
                <input
                  type="number"
                  value="0.0"
                  name="advip_washout_description_cr"
                  style="width: 100px"
                />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Variation</span>
              </div>
              <div class="col">
                <select name="advip_washout_description_variation" v-model="washout_variation">
                  <option value="QUADRATIC">Quadratic</option>
                  <option value="LINEAR">Linear</option>
                  <option value="USER_DEFINED">User Defined</option>
                </select>
                <input
                  type="text"
                  value="1,2,7,12"
                  name="ud_wo_variation"
                  v-show="washout_variation==='USER_DEFINED'"
                />
              </div>
            </div>
          </fieldset>
          <br />
          <fieldset>
            <legend>Side Flap Description</legend>
            <div class="row">
              <div class="col">
                <span>Rear <span class="d-none d-sm-inline-block">Edge Length</span></span>
              </div>
              <div class="col">
                <input type="number" value="10.0" name="advip_sfd_rel" style="width: 100px" />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Front <span class="d-none d-sm-inline-block">Edge Length</span></span>
              </div>
              <div class="col">
                <input type="number" value="20.0" name="advip_sfd_fel" style="width: 100px" />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Index</span>
              </div>
              <div class="col">
                <input type="number" value="0.0" name="advip_sfd_index" style="width: 100px" />
              </div>
            </div>
          </fieldset>
          <br />
          <fieldset>
            <legend>Transform Geometry</legend>
            <div class="row">
              <div class="col">
                <span>Rotation Axis (x,y,z)</span>
              </div>
              <div class="col">
                <input type="text" value="0,0,0" name="advip_tg_ra" style="width: 100px" />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Translation Axis (x,y,z)</span>
              </div>
              <div class="col">
                <input type="text" value="0,0,0" name="advip_tg_ta" style="width: 100px" />
              </div>
            </div>
          </fieldset>
          <br />
          <fieldset>
            <legend>Slider</legend>
            <div class="row">
              <div class="col">
                <span>Area Percentage</span>
              </div>
              <div class="col">
                <input type="number" value="2" name="advip_slider_ap" style="width: 100px" />
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Width Length Ratio</span>
              </div>
              <div class="col">
                <input type="number" value="0.5" name="advip_slider_wlr" style="width: 100px" />
              </div>
            </div>
          </fieldset>
          <br />
          <fieldset>
            <legend>Mesh Parameter</legend>
            <div class="row">
              <div class="col">
                <span>Mesh Size (% of chord)</span>
              </div>
              <div class="col">
                <input type="number" value="3.0" name="advip_others_ms" style="width: 100px" />
              </div>
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
      washout_variation: "QUADRATIC"
    };
  },
  created() {
    EventBus.$on("input_param_ai_got_clicked", input_param_ai_flag => {
      this.input_toggle = input_param_ai_flag;
    });
  }
};
</script>
