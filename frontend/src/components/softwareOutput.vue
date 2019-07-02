<template>
  <div id="output_screen">
    <div id="view_toolbar">
      <ul>
        <li v-bind:class="{toolbar_active:drawing_3d_flag}" v-on:click="drawing_3d_flag=true">3D</li>
        <li v-bind:class="{toolbar_active:!drawing_3d_flag}" v-on:click="drawing_3d_flag=false">2D</li>
      </ul>
    </div>
    <div id="softwareOutput" class="card" v-bind:class="{display_none_element:!drawing_3d_flag}">
      <!--<img class="card-img-top" src="../assets/images/p1.jpg">-->
      <div class="content"></div>
      <div id="loader">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
        <div class="bar4"></div>
        <div class="bar5"></div>
        <div class="bar6"></div>
      </div>
    </div>
    <div id="dxf_output" v-if="!drawing_3d_flag">
      <button class="btn btn-success">Download DXF</button>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      drawing_3d_flag: true
    };
  }
};
</script>