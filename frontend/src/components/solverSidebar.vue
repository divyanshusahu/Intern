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
        <a href="#" v-on:click="stop_solver">Stop Solver</a>
      </li>
      <li>
        <a href="#" v-on:click="sidebar_run_clicked">Run Parez</a>
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
      solver_flag : true,
      run_flag : false
		};
	},
	created() {
      EventBus.$on('sidebar_flag_got_clicked', (sidebar_collapse_flag) => {
        this.sidebar_toggle = sidebar_collapse_flag;
      });
  },
  methods : {
    sidebar_run_clicked : function() {
      this.run_flag = true;
      EventBus.$emit("sidebar_run_got_clicked", this.run_flag);
      this.run_flag = false;
    },
    stop_solver : function() {
      EventBus.$on("solver_overall_resuslt", (solver_result) => {
        this.axios.post('/api/job_cancel', solver_result).then((data) => {
          console.log(data);
        });
      });
    }
  }
}
</script>
