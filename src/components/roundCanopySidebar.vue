<template>
  <li>
    <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
    v-on:click="round_canopy_flag = !round_canopy_flag">
    <i class="fas fa-circle-notch"></i>Round Canopy</a>
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
      round_canopy_flag : true,
      rc_input_param_flag : false
    };
  },
  methods : {
    got_clicked : function() {
      //this.rc_input_param_flag = !this.rc_input_param_flag;
      EventBus.$emit('rc_input_param_got_clicked', this.rc_input_param_flag);
    }
  }
}
</script>
