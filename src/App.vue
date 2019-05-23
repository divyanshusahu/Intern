<template>
  
  <div id="app">

    <div class="wrapper">
      <sidebar />
      <div id="content">
        <topbar />
        <softwareOutput />
      </div>
    </div>

  </div>

</template>

<script>
import sidebar from './components/sidebar.vue'
import topbar from './components/topbar.vue'
import softwareOutput from './components/softwareOutput.vue'

export default {
  name: 'app',
  components: {
    sidebar,
    topbar,
    softwareOutput
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;
  color: #2c3e50;
  margin-top: 60px;*/
}

::-webkit-scrollbar {width: 6px; height: 4px; background: rgba(0,0,0,0.8); }
::-webkit-scrollbar-thumb { background-color: rgba(0,0,0,0.8); }

@import 'assets/css/wrapper.css';
@import 'assets/css/sidebar.css';
@import 'assets/css/topbar.css';
@import 'assets/css/softwareOutput.css';

</style>
