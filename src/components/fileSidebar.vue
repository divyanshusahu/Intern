<template>
    <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
        v-on:click="file_flag = !file_flag">File</a>
        <ul class="list-unstyled" id="file" v-bind:class="{collapse: file_flag}">
          <li>
            <a href="#">New</a>
          </li>
          <li>
            <a href="#">Open</a>
          </li>
          <li>
            <a href="#">Import VTK</a>
          </li>
          <li class="divider"></li>
          <li>
            <a href="#">Exit</a>
          </li>
        </ul>
      </li>
</template>

<script>
export default {
    data : function() {
      return {
        file_flag : true
      };
    }
}
</script>
