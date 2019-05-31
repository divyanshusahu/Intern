<template>
  <li>
    <!--<a href="#" data-toggle="collapse" aria-expended="false" class=""
    v-bind:class="{'dropdown-toggle' : !sidebar_toggle}"
    v-on:click="round_canopy_flag = !round_canopy_flag">
    <i class="fas fa-circle-notch"></i><strong>Round Canopy</strong></a>-->
    <a href="#" v-on:click="round_canopy_flag = !round_canopy_flag">
          <i class="fas fa-circle-notch sidebar_icons"></i><strong>Round Canopy</strong>
          <i class="fas downmenu_icon" 
          v-bind:class="{toggle_dropdown_menu : !round_canopy_flag, 'fa-caret-down': !sidebar_toggle}"></i>
        </a>
    <ul class="list-unstyled" id="round_canopy" v-bind:class="{collapse: round_canopy_flag}">
      <li>
        <a href="#" id="btn_round_canopy" v-on:click="got_clicked">Input Parameter</a>
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
      round_canopy_flag : true,
      rc_input_param_flag : false
    };
  },
  methods : {
    got_clicked : function() {
      //this.rc_input_param_flag = !this.rc_input_param_flag;
      EventBus.$emit('rc_input_param_got_clicked', this.rc_input_param_flag);
    }
  },
  created() {
      EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
        this.sidebar_toggle = sidebar_collapse_flag;
      });
    }
}
</script>
