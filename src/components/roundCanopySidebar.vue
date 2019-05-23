<template>
  <li>
    <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
    v-on:click="round_canopy_flag = !round_canopy_flag">
    <i class="fas fa-circle-notch"></i>Round Canopy</a>
    <ul class="list-unstyled" id="round_canopy" v-bind:class="{collapse: round_canopy_flag}">
      <li>
        <a href="#" id="btn_round_canopy">Input Parameter</a>
      </li>
    </ul>
  </li>
</template>

<script>
export default {
  data : function() {
    return {
      round_canopy_flag : true
    };
  }
}
</script>
