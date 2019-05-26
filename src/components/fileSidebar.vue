<template>
    <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class=""
        v-on:click="file_flag = !file_flag" v-bind:class="{'dropdown-toggle' : !sidebar_toggle}">
        <i class="fas fa-file"></i><strong>File</strong></a>
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
import { EventBus } from '../main.js';
export default {
    data : function() {
      return {
        file_flag : true,
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
