<template>
  <li>
    <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
    v-on:click="help_flag = !help_flag"><i class="fas fa-info"></i>Help</a>
    <ul class="list-unstyled" id="help" v-bind:class="{collapse : help_flag}">
      <li>
        <a href="#">Manual</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
    </ul>
  </li>
</template>

<script>
export default {
  data : function() {
    return {
      help_flag : true
    };
  }
}
</script>
