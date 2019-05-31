<template>
  <li>
    <!--<a href="#" data-toggle="collapse" aria-expended="false" class="" 
    v-bind:class="{'dropdown-toggle' : !sidebar_toggle}"
    v-on:click="help_flag = !help_flag"><i class="fas fa-info"></i><strong>Help</strong></a>-->
    <a href="#" v-on:click="help_flag = !help_flag">
          <i class="fas fa-info sidebar_icons"></i><strong>Help</strong>
          <i class="fas downmenu_icon" 
          v-bind:class="{toggle_dropdown_menu : !help_flag, 'fa-caret-down': !sidebar_toggle}"></i>
    </a>
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
import { EventBus } from '../main.js';
export default {
  data : function() {
    return {
      help_flag : true,
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
