<template>
  <div class="custom_modal" id="flat_panels_modal" v-bind:class="{pop_up_toggle : input_toggle}">
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Panel Input
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <b>Sewing Allowance</b>
          <div class="row">
            <div class="col">
              <p>Max Value (mm)</p>
            </div>
            <div class="col">
              <input
                type="number"
                value="50.0"
                name="flat_panels_sa_max_value"
                style="width: 100px"
              >
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Min Value (mm)</p>
            </div>
            <div class="col">
              <input type="number" value="1.0" name="flat_panels_sa_min_value" style="width: 100px">
            </div>
          </div>
          <br>
          <b>Sewing Allowance for Ribs</b>
          <div class="row">
            <div class="col">
              <p>Sides (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sar_sides" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Front (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sar_front" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Rear (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sar_rear" style="width: 100px">
            </div>
          </div>
          <br>
          <b>Sewing Allowance Panel</b>
          <div class="row">
            <div class="col">
              <p>Sides (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sap_sides" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Front (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sap_front" style="width: 100px">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <p>Rear (% of chord)</p>
            </div>
            <div class="col">
              <input type="number" value="2.0" name="flat_panels_sap_rear" style="width: 100px">
            </div>
          </div>
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
      flat_panels_obj: {}
    };
  },
  created() {
    EventBus.$on("input_param_fp_got_clicked", input_param_fp_flag => {
      this.input_toggle = input_param_fp_flag;
    });

    EventBus.$on("run_got_clicked", run_clicked_flag => {
      if (run_clicked_flag) {
        this.flat_panels_obj["drawing_2d"] = {
          file_name: "/work/ram_2d_drawing.dxf",
          sewing_allowance: {
            panel_rear_percentc: parseFloat(
              document.getElementsByName("flat_panels_sap_rear")[0].value
            ),
            max_value: parseFloat(
              document.getElementsByName("flat_panels_sa_max_value")[0].value
            ),
            min_value: parseFloat(
              document.getElementsByName("flat_panels_sa_min_value")[0].value
            ),
            rib_rear_percentc: parseFloat(
              document.getElementsByName("flat_panels_sar_rear")[0].value
            ),
            rib_front_percentc: parseFloat(
              document.getElementsByName("flat_panels_sar_front")[0].value
            ),
            panel_front_percentc: parseFloat(
              document.getElementsByName("flat_panels_sap_front")[0].value
            ),
            panel_sides_percentc: parseFloat(
              document.getElementsByName("flat_panels_sap_sides")[0].value
            ),
            rib_sides_percentc: parseFloat(
              document.getElementsByName("flat_panels_sar_sides")[0].value
            )
          }
        };
        EventBus.$emit("inputParamFP_obj", this.flat_panels_obj);
      }
    });
  }
};
</script>