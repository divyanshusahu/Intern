<template>
  <div class="custom_modal" id="volute_modal" v-bind:class="{pop_up_toggle: input_toggle}">
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Volute Input
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <fieldset>
            <legend>Volute</legend>
            <div class="row">
              <div class="col">
                <span>Shape</span>
              </div>
              <div class="col">
                <span>Elliptic</span>
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Minot to Major axis ratio</span>
              </div>
              <div class="col">
                <input type="number" value="1.0" name="volute_input_minot_ratio" style="width:100px;">
              </div>
            </div>
            <div class="row">
              <div class="col">
                <span>Semi Span Angle (deg)</span>
              </div>
              <div class="col">
                <input type="number" value="45.0" name="volute_input_ssa" style="width: 100px">
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
      volute_obj: {}
    };
  },
  created() {
    EventBus.$on("input_param_volute_got_clicked", input_param_volute_flag => {
      this.input_toggle = input_param_volute_flag;
    });

    EventBus.$on("run_got_clicked", run_clicked_flag => {
      if (run_clicked_flag) {
        this.volute_obj["volute_description"] = {
          shape: "ELLIPTIC",
          semi_span_angle: parseFloat(
            document.getElementsByName("volute_input_ssa")[0].value
          ),
          minor_to_major_axes: parseFloat(
            document.getElementsByName("volute_input_minot_ratio")[0].value
          )
        };
        EventBus.$emit("inputParamVOLUTE_obj", this.volute_obj);
      }
    });
  }
};
</script>