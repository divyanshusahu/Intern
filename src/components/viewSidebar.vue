<template>
  <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class=""
        v-bind:class="{'dropdown-toggle' : !sidebar_toggle}" 
        v-on:click="view_flag = !view_flag">
        <i class="fas fa-eye"></i><strong>View</strong></a>
        <ul class="list-unstyled" id="view" v-bind:class="{collapse: view_flag}">
          <li>
            <a href="#">Default</a>
          </li>
          <li>
            <a href="#">Isomeric</a>
          </li>
          <li>
            <a href="#">Front View</a>
          </li>
          <li>
            <a href="#">Back View</a>
          </li>
          <li>
            <a href="#">Left View</a>
          </li>
          <li>
            <a href="#">Right View</a>
          </li>
          <li>
            <a href="#">Top View</a>
          </li>
          <li>
            <a href="#">Bottom View</a>
          </li>
        </ul>
      </li>
</template>

<script>
import { EventBus } from '../main.js';
export default {
  data : function() {
    return {
      sidebar_toggle : null,
      view_flag: true
    };
  },
  created() {
      EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
        this.sidebar_toggle = sidebar_collapse_flag;
      });
    }
}
</script>
