<template>
  <li>
    <a href="#" v-on:click="input_parameter_flag = !input_parameter_flag">
      <i class="fas fa-keyboard sidebar_icons"></i>
      <strong>Input Parameter</strong>
      <i
        class="fas downmenu_icon"
        v-bind:class="{toggle_dropdown_menu : !input_parameter_flag, 'fa-caret-down': !sidebar_toggle}"
      ></i>
    </a>
    <ul class="list-unstyled" id="input_parameter" v-bind:class="{collapse: input_parameter_flag}">
      <li v-on:click="got_clicked_planform">
        <!--<img src="../assets/icon/planform_selected.svg" alt="Planform" height="40" width="40"/>-->
        <a href="#" id="btn_planform">PlanForm</a>
      </li>
      <li v-on:click="got_clicked_airfoil">
        <!--<img src="../assets/icon/airfoil_i.svg" alt="Airfoil" height="40" width="40"/>-->
        <a href="#" id="btn_airfoil">Airfoil</a>
      </li>
      <li v-on:click="got_clicked_volute">
        <!--<img src="../assets/icon/volute_selected.svg" alt="Volute" height="40" width="40"/>-->
        <a href="#" id="btn_volute">Volute</a>
      </li>
      <li v-on:click="got_clicked_al">
        <!--<img src="../assets/icon/anchor_selected.svg" alt="Anchor Location" height="40" width="40"/>-->
        <a href="#" id="btn_anchor_location">Anchor Location</a>
      </li>
      <li v-on:click="got_clicked_fp">
        <!--<img src="../assets/icon/panels_selected.svg" alt="Flat Panels" height="40" width="40"/>-->
        <a href="#" id="btn_flat_panels">Flat Panels</a>
      </li>
      <li v-on:click="got_clicked_rla">
        <!--<img src="../assets/icon/riserlines_selected.svg" alt="Riserlines" height="40" width="40"/>-->
        <a href="#" id="btn_rigging_lines_arrangement">Rigging Lines</a>
      </li>
      <li v-on:click="got_clicked_brake_lines">
        <!--<img src="../assets/icon/brake_selected.svg" alt="Brake Lines" height="40" width="40"/>-->
        <a href="#" id="btn_brake_lines">Brake Lines</a>
      </li>
      <li class="divider"></li>
      <li v-on:click="got_clicked_ai">
        <a href="#" id="btn_advance_input">Advance Input</a>
      </li>
    </ul>
  </li>
</template>

<script>
import { EventBus } from "../main.js";
export default {
  data: function() {
    return {
      sidebar_toggle: null,
      input_parameter_flag: true,
      input_param_planform_flag: false,
      input_param_airfoil_flag: false,
      input_param_volute_flag: false,
      input_param_al_flag: false,
      input_param_fp_flag: false,
      input_param_rla_flag: false,
      input_param_brake_lines_flag: false,
      input_param_ai_flag: false
    };
  },
  methods: {
    got_clicked_planform: function() {
      EventBus.$emit(
        "input_param_planform_got_clicked",
        this.input_param_planform_flag
      );
    },
    got_clicked_airfoil: function() {
      EventBus.$emit(
        "input_param_airfoil_got_clicked",
        this.input_param_airfoil_flag
      );
    },
    got_clicked_volute: function() {
      EventBus.$emit(
        "input_param_volute_got_clicked",
        this.input_param_volute_flag
      );
    },
    got_clicked_al: function() {
      EventBus.$emit("input_param_al_got_clicked", this.input_param_al_flag);
    },
    got_clicked_fp: function() {
      EventBus.$emit("input_param_fp_got_clicked", this.input_param_fp_flag);
    },
    got_clicked_rla: function() {
      EventBus.$emit("input_param_rla_got_clicked", this.input_param_rla_flag);
    },
    got_clicked_brake_lines: function() {
      EventBus.$emit(
        "input_param_brake_lines_got_clicked",
        this.input_param_brake_lines_flag
      );
    },
    got_clicked_ai: function() {
      EventBus.$emit("input_param_ai_got_clicked", this.input_param_ai_flag);
    }
  },
  created() {
    EventBus.$on("sidebar_flag_got_clicked", sidebar_collapse_flag => {
      this.sidebar_toggle = sidebar_collapse_flag;
    });
  }
};
</script>