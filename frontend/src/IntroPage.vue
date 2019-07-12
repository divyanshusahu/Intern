<template>
  <div id="introPage">
    <introHeader />
    <introMain />
  </div>
</template>

<script>
import introHeader from './introComponents/introHeader.vue';
import introMain from './introComponents/introMain';

export default {
  name : 'introPage',
  components : {
    introHeader,
    introMain
  }
}

require('./assets/js/argon.js');
</script>

<style>
@import './assets/css/nucleo.css';
@import './assets/css/argon.css?v=1.1.0';
</style>
