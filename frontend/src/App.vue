<template>
  
  <div id="app">

    <div class="wrapper">
      <sidebar />
      <div id="content">
        <div class="small_screen_overlay"
          v-touch:swipe.left="sidebar_swipe_toggle" 
          v-touch:tap="sidebar_swipe_toggle"
        >
        </div>
        <topbar />
        <softwareOutput />
        <outputLog />
      </div>
    </div>

    <allInputs />

  </div>

</template>

<script>
import sidebar from './components/sidebar.vue'
import topbar from './components/topbar.vue'
import softwareOutput from './components/softwareOutput.vue'
import outputLog from './components/outputLog.vue'
import allInputs from './components/allInputs.vue'

import { EventBus } from './main.js'

export default {
  name: 'app',
  components: {
    sidebar,
    topbar,
    softwareOutput,
    outputLog,
    allInputs
  },
  data : function() {
    return {
      swipe : null
    }
  },
  methods : {
    sidebar_swipe_toggle : function() {
      this.swipe = true;
      document.getElementsByClassName("small_screen_overlay")[0].style.display = "none";
      EventBus.$emit("android_swipe_toggle", this.swipe);
    }
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}

::-webkit-scrollbar {width: 6px; height: 4px; background: rgba(0,0,0,0.4); }
::-webkit-scrollbar-thumb { background-color: rgba(0,0,0,0.4); }

@import 'assets/css/wrapper.css';
@import 'assets/css/sidebar.css';
@import 'assets/css/topbar.css';
@import 'assets/css/softwareOutput.css';
@import 'assets/css/outputLog.css';
@import 'assets/css/customModal.css';
@import 'assets/css/smallScreen.css';

</style>
