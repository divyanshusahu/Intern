<template>
  <div
    class="custom_modal"
    id="rigging_lines_arrangment_modal"
    v-bind:class="{pop_up_toggle : input_toggle}"
  >
    <div class="card bg-light input_popup">
      <div class="card-header">
        <h5>
          Rigging Lines Arrangment
          <span v-on:click="input_toggle = !input_toggle">&times;</span>
        </h5>
      </div>
      <div class="card-body">
        <div class="container-fluid">
          <fieldset>
            <legend>Chordwise Location</legend>
            <div class="row">
              <div class="col">
                <p>Location (% of chord)</p>
              </div>
              <div class="col">
                <input
                  type="text"
                  value="1.0,35.0,75.0,90.0"
                  name="rla_cl_location"
                  style="width: 100%"
                >
              </div>
            </div>
            <div class="row">
              <div class="col">
                <p>Suspension Length(mm)</p>
              </div>
              <div class="col">
                <input type="number" value="6800.0" name="rla_cl_susplen" style="width: 100%">
              </div>
            </div>
            <div class="row">
              <div class="col">
                <p>Distance between Karabiners Length</p>
              </div>
              <div class="col">
                <input type="number" value="400.0" name="advip_others_dkl" style="width: 100px">
              </div>
            </div>
          </fieldset>
          <br>
          <div class="row">
            <div class="col-sm-12 col-md-6 card">
              <div class="card-body user_define" >
              <span>L1 Combination</span>
              <input type="checkbox" name="is_rla_l1" style="width:20%;" v-model="rla_l1">
                <br>
                <div v-bind:class="{disabledDiv:!rla_l1}">
                  <span>L1 Length</span>
                  <input type="text" name="rla_l1_length" value="20" style="width:20%;">
                  <div class="custom_user_define_inputs" id="l1_rla">
                    <input type="text" value="0,1" name="rla_l1_inputs">
                    <input type="text" value="2,3" name="rla_l1_inputs">
                  </div>
                  <div class="user_define_add_remove_buttons">
                    <button
                      type="button"
                      class="btn btn-sm btn-secondary"
                      v-on:click="remove_l1_user_define"
                    >Remove</button>
                    <button
                      type="button"
                      class="btn btn-sm btn-secondary"
                      v-on:click="add_l1_user_define"
                    >Add</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-sm-12 col-md-6 card">
              <div class="card-body user_define">
                <span>L2 Combination</span>
                <input type="checkbox" name="is_rla_l2" style="width:20%;" v-model="rla_l2">
                <br>
                <div v-bind:class="{disabledDiv:!rla_l2}">
                  <span>L2 Length</span>
                  <input type="text" name="rla_l2_length" value="20" style="width:20%;">
                  <div class="custom_user_define_inputs" id="l2_rla">
                    <input type="text" value="1,2,4" name="rla_l2_inputs">
                    <input type="text" value="3,5,8" name="rla_l2_inputs">
                  </div>
                  <div class="user_define_add_remove_buttons">
                    <button
                      type="button"
                      class="btn btn-sm btn-secondary"
                      v-on:click="remove_l2_user_define"
                    >Remove</button>
                    <button
                      type="button"
                      class="btn btn-sm btn-secondary"
                      v-on:click="add_l2_user_define"
                    >Add</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-footer">
        <button
          type="button"
          class="btn btn-success"
          v-on:click="input_toggle = !input_toggle"
        >Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import { EventBus } from "../main.js";

export default {
  data: function() {
    return {
      input_toggle: true,
      rla_l1: '',
      rla_l2: '',
    };
  },
  methods: {
    add_l1_user_define: function() {
      let inp_node = document.createElement("input");
      inp_node.setAttribute("type", "text");
      inp_node.setAttribute("name", "rla_l1_inputs");
      document.getElementById("l1_rla").appendChild(inp_node);
    },
    remove_l1_user_define: function() {
      let last_child = document.getElementById("l1_rla").lastChild;
      document.getElementById("l1_rla").removeChild(last_child);
    },
    add_l2_user_define: function() {
      let inp_node = document.createElement("input");
      inp_node.setAttribute("type", "text");
      inp_node.setAttribute("name", "rla_l2_inputs");
      document.getElementById("l2_rla").appendChild(inp_node);
    },
    remove_l2_user_define: function() {
      let last_child = document.getElementById("l2_rla").lastChild;
      document.getElementById("l2_rla").removeChild(last_child);
    }
  },
  created() {
    EventBus.$on("input_param_rla_got_clicked", input_param_rla_flag => {
      this.input_toggle = input_param_rla_flag;
    });
  }
};
</script>