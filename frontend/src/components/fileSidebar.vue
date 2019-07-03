<template>
  <li>
    <a href="#" v-on:click="file_flag = !file_flag">
      <i class="fas fa-file sidebar_icons"></i><strong>File</strong>
      <i class="fas downmenu_icon" 
      v-bind:class="{toggle_dropdown_menu : !file_flag, 'fa-caret-down': !sidebar_toggle}"></i>
    </a>
    <ul class="list-unstyled" id="file" v-bind:class="{collapse: file_flag}">
      <li>
      <a href="#" v-on:click="remove_output">New</a>
      </li>
      <li>
      <a href="#" v-on:click="local_vtp_open">Open
        <input id="vtp_file_input" type="file" accept=".vtp" style="display:none;" />
      </a>
      </li>
      <li>
      <a href="#" v-on:click="save_input_file">Save Input</a>
      </li>
    </ul>
    </li>
</template>

<script>
import { EventBus } from '../main.js';
import { initLocalFileLoader } from '../vtkview.js';
import { save_input } from '../save_inputs.js';
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
  },
  methods : {
    remove_output : function() {
    document.getElementById("vtp_file_input").value = "";
    var outDiv = document.getElementById("softwareOutput");
    if (outDiv.children[0].children.length){
      outDiv.removeChild(outDiv.getElementsByTagName("div")[0]);
      let a = document.createElement('div');
      a.setAttribute('class', 'content');
      outDiv.insertBefore(a, outDiv.firstChild);
      outDiv.style.backgroundColor = "#fff";
    }
    },
    local_vtp_open : function() {
    document.getElementById("vtp_file_input").click();
    initLocalFileLoader();
    },
    save_input_file : function() {
      save_input();
    }
  }
}
</script>
