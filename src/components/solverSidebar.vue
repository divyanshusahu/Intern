<template>
    <li>
  	<!--<a href="#" data-toggle="collapse" aria-expended="false" class=""
		v-bind:class="{'dropdown-toggle' : !sidebar_toggle}"
		v-on:click="solver_flag = !solver_flag"><i class="fas fa-play"></i><strong>Solver</strong></a>-->
    <a href="#" v-on:click="solver_flag = !solver_flag">
          <i class="fas fa-play sidebar_icons"></i><strong>Solver</strong>
          <i class="fas downmenu_icon" 
          v-bind:class="{toggle_dropdown_menu : !solver_flag, 'fa-caret-down': !sidebar_toggle}"></i>
        </a>
    <ul class="list-unstyled" id="solver" v-bind:class="{collapse : solver_flag}">
      <li>
        <a href="#">Stop Solver</a>
      </li>
      <li>
        <a href="#">Run Parez</a>
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
			solver_flag : true
		};
	},
	created() {
      EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
        this.sidebar_toggle = sidebar_collapse_flag;
      });
    }
}
</script>
