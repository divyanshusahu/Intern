<template>
  <nav id="sidebar" v-bind:class="{active: sidebar_toggle}">
    <div class="sidebar-header">
      <h3 style="text-align: center;">SOFTWARE</h3>
      <strong>SN</strong>
      <i
        class="far fa-arrow-alt-circle-left d-inline-block d-lg-none"
        style="float: right; font-size: 1.5em;"
        v-on:click="mobile_sidebar_got_clicked"
      ></i>
    </div>

    <ul class="list-unstyled components">
      <fileSidebar/>
      <viewSidebar/>
      <inputParameterSidebar/>
      <roundCanopySidebar/>
      <solverSidebar/>
      <helpSidebar/>
    </ul>
  </nav>
</template>

<script>
import { EventBus } from "../main.js";

import fileSidebar from "./fileSidebar.vue";
import viewSidebar from "./viewSidebar.vue";
import inputParameterSidebar from "./inputParameterSidebar.vue";
import roundCanopySidebar from "./roundCanopySidebar.vue";
import solverSidebar from "./solverSidebar.vue";
import helpSidebar from "./helpSidebar.vue";

export default {
  components: {
    fileSidebar,
    viewSidebar,
    inputParameterSidebar,
    roundCanopySidebar,
    solverSidebar,
    helpSidebar
  },
  data: function() {
    return {
      sidebar_toggle: null
    };
  },
  created() {
    EventBus.$on("sidebar_flag_got_clicked", sidebar_collapse_flag => {
      this.sidebar_toggle = sidebar_collapse_flag;
    });
    EventBus.$on("android_swipe_toggle", (swipe) => {
      if (this.sidebar_toggle == true)
        this.sidebar_toggle = !swipe;
    });
  },
  methods: {
    mobile_sidebar_got_clicked: function() {
      this.sidebar_toggle = !this.sidebar_toggle;
      EventBus.$emit("mobile_sidebar_toggle", this.sidebar_toggle);
    }
  }
};
</script>
