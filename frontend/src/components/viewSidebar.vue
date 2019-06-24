<template>
  <li>
        <!--<a href="#" data-toggle="collapse" aria-expended="false" class=""
        v-bind:class="{'dropdown-toggle' : !sidebar_toggle}" 
        v-on:click="view_flag = !view_flag">
        <i class="fas fa-eye"></i><strong>View</strong></a>-->
        <a href="#" v-on:click="view_flag = !view_flag">
          <i class="fas fa-eye sidebar_icons"></i><strong>View</strong>
          <i class="fas downmenu_icon" 
          v-bind:class="{toggle_dropdown_menu : !view_flag, 'fa-caret-down': !sidebar_toggle}"></i>
        </a>
        <ul class="list-unstyled" id="view" v-bind:class="{collapse: view_flag}">
          <li>
            <a href="#" v-on:click="camera_view('front')">Default</a>
          </li>
          <li>
            <a href="#">Isomeric</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('front')">Front View</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('back')">Back View</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('left')">Left View</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('right')">Right View</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('top')">Top View</a>
          </li>
          <li>
            <a href="#" v-on:click="camera_view('bottom')">Bottom View</a>
          </li>
        </ul>
      </li>
</template>

<script>
import { EventBus } from '../main.js';
import { change_camera_view } from "../vtkview.js";
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
  },
  methods : {
    camera_view : function(view) {
      change_camera_view(view);
    }
  }
}
</script>
