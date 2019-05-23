<template>
  <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
        v-on:click="input_parameter_flag = !input_parameter_flag">Input Parameter</a>
        <ul class="list-unstyled" id="input_parameter" v-bind:class="{collapse: input_parameter_flag}">
          <li>
            <a href="#" id="btn_planform">PlanForm</a>
          </li>
          <li>
            <a href="#" id="btn_airfoil">Airfoil</a>
          </li>
          <li>
            <a href="#" id="btn_volute">Volute</a>
          </li>
          <li>
            <a href="#" id="btn_anchor_location">Anchor Location</a>
          </li>
          <li>
            <a href="#" id="btn_flat_panels">Flat Panels</a>
          </li>
          <li>
            <a href="#" id="btn_rigging_lines_arrangement">Rigging Lines Arrangement</a>
          </li>
          <li>
            <a href="#" id="btn_brake_lines">Brake Lines</a>
          </li>
          <li>
            <a href="#">Run</a>
          </li>
          <li class="divider"></li>
          <li>
            <a href="#" id="btn_advance_input">Advance Input</a>
          </li>
        </ul>
      </li>
</template>

<script>
export default {
  data : function() {
    return {
      input_parameter_flag: true
    };
  }  
}
</script>

