<template>
  
	<nav id="sidebar" v-bind:class="{active: sidebar_toggle}">
    
		<div class="sidebar-header">
      <h3 style="text-align: center;">RAM AIR PARACHUTE</h3>
    </div>

    <ul class="list-unstyled components">
      <fileSidebar />
      <viewSidebar />
      <inputParameterSidebar />
      <roundCanopySidebar />
      <solverSidebar />
      <helpSidebar />
    </ul>
  
  </nav>
</template>

<script>
import { EventBus } from '../main.js';

import fileSidebar from './fileSidebar.vue'
import viewSidebar from './viewSidebar.vue'
import inputParameterSidebar from './inputParameterSidebar.vue'
import roundCanopySidebar from './roundCanopySidebar.vue'
import solverSidebar from './solverSidebar.vue'
import helpSidebar from './helpSidebar.vue'

export default {
  components : {
    fileSidebar,
    viewSidebar,
    inputParameterSidebar,
    roundCanopySidebar,
    solverSidebar,
    helpSidebar
  },
  data : function() {
    return {
      sidebar_toggle : null
      };
  },
  created() {
    EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
      this.sidebar_toggle = sidebar_collapse_flag;
    });
  }
}
</script>
