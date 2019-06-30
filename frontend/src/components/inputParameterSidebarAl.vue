<template>
  <div
    class="custom_modal"
    id="anchor_location_modal"
    v-bind:class="{pop_up_toggle : input_toggle}"
  >
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Anchor Description
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <p>Ribs Connection</p>
        <input name="ribs_connection" type="radio" value="ALL" v-model="user_define"> All Ribs
        <br>
        <input name="ribs_connection" type="radio" value="ALTERNATE" v-model="user_define"> Alternative Ribs
        <br>
        <input name="ribs_connection" type="radio" value="USER_DEFINED" v-model="user_define"> User Define
        <input
          type="text"
          name="user_defined_ribs"
          value="1,3,5,7"
          v-if="user_define==='USER_DEFINED'"
        >
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
      user_define: "ALL",
      ribs: {}
    };
  },
  created() {
    EventBus.$on("input_param_al_got_clicked", input_param_al_flag => {
      this.input_toggle = input_param_al_flag;
    });

    EventBus.$on("run_got_clicked", run_clicked_flag => {
      if (run_clicked_flag) {
        this.ribs["alv"] = this.user_define;
        this.ribs["udr"] = [1, 3, 8, 13];
        if (this.user_define === "USER_DEFINED") {
          this.ribs["udr"] = document
            .getElementsByName("user_defined_ribs")[0]
            .value.split(",")
            .map(function(x) {
              return parseInt(x) - 1;
            });
        }
        EventBus.$emit("inputParamAL_obj", this.ribs);
      }
    });
  }
};
</script>