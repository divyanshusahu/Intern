<template>
  <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class=""
        v-bind:class="{'dropdown-toggle' : !sidebar_toggle}"
        v-on:click="input_parameter_flag = !input_parameter_flag">
        <i class="fas fa-keyboard"></i><strong>Input Parameter</strong></a>
        <ul class="list-unstyled" id="input_parameter" v-bind:class="{collapse: input_parameter_flag}">
          <li v-on:click="got_clicked_planform">
            <a href="#" id="btn_planform">PlanForm</a>
          </li>
          <li v-on:click="got_clicked_airfoil">
            <a href="#" id="btn_airfoil">Airfoil</a>
          </li>
          <li v-on:click="got_clicked_volute">
            <a href="#" id="btn_volute">Volute</a>
          </li>
          <li v-on:click="got_clicked_al">
            <a href="#" id="btn_anchor_location">Anchor Location</a>
          </li>
          <li v-on:click="got_clicked_fp">
            <a href="#" id="btn_flat_panels">Flat Panels</a>
          </li>
          <li v-on:click="got_clicked_rla">
            <a href="#" id="btn_rigging_lines_arrangement">Rigging Lines Arrangement</a>
          </li>
          <li v-on:click="got_clicked_brake_lines">
            <a href="#" id="btn_brake_lines">Brake Lines</a>
          </li>
          <li>
            <a href="#">Run</a>
          </li>
          <li class="divider"></li>
          <li v-on:click="got_clicked_ai">
            <a href="#" id="btn_advance_input">Advance Input</a>
          </li>
        </ul>
      </li>
</template>

<script>
import { EventBus } from '../main.js';
export default {
  data : function() {
    return {
      sidebar_toggle : null,
      input_parameter_flag: true,
      input_param_planform_flag : false,
      input_param_airfoil_flag : false,
      input_param_volute_flag : false,
      input_param_al_flag : false,
      input_param_fp_flag : false,
      input_param_rla_flag : false,
      input_param_brake_lines_flag : false,
      input_param_ai_flag : false
    };
  },
  methods : {
    got_clicked_planform : function() {
      EventBus.$emit("input_param_planform_got_clicked", this.input_param_planform_flag);
    },
    got_clicked_airfoil : function() {
      EventBus.$emit("input_param_airfoil_got_clicked", this.input_param_airfoil_flag);
    },
    got_clicked_volute : function() {
      EventBus.$emit("input_param_volute_got_clicked", this.input_param_volute_flag);
    },
    got_clicked_al : function() {
      EventBus.$emit("input_param_al_got_clicked", this.input_param_al_flag);
    },
    got_clicked_fp : function() {
      EventBus.$emit("input_param_fp_got_clicked", this.input_param_fp_flag);
    },
    got_clicked_rla : function() {
      EventBus.$emit("input_param_rla_got_clicked", this.input_param_rla_flag);
    },
    got_clicked_brake_lines : function() {
      EventBus.$emit("input_param_brake_lines_got_clicked", this.input_param_brake_lines_flag);
    },
    got_clicked_ai : function() {
      EventBus.$emit("input_param_ai_got_clicked", this.input_param_ai_flag);
    }
  },
  created() {
      EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
        this.sidebar_toggle = sidebar_collapse_flag;
      });
    } 
}
</script>

