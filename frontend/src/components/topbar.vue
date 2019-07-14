<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <button
        type="button"
        id="sidebarCollapse"
        class="navbar-btn"
        v-bind:class="{active: sidebar_collapse_flag}"
        v-on:click="got_clicked"
      >
        <i class="far fa-arrow-alt-circle-left"></i>
        <span></span>
        <span></span>
        <span></span>
      </button>

      <span class="d-block d-lg-none mobile_inputs_icons">
        <img
          src="../assets/icon/planform.png"
          alt="Planform"
          title="Planform"
          v-on:click="got_clicked_planform"
        />
        <img
          src="../assets/icon/airfoil.png"
          alt="Airfoil"
          title="Airfoil"
          v-on:click="got_clicked_airfoil"
        />
        <img src="../assets/icon/volute.png" alt="Volute" title="Volute" 
          v-on:click="got_clicked_volute" />
        <img src="../assets/icon/anchor.png" alt="Anchor" title="Anchor"
          v-on:click="got_clicked_al" />
        <img src="../assets/icon/panels.png" alt="Panels" title="Panels"
          v-on:click="got_clicked_fp" />
        <img
          src="../assets/icon/riserlines.png"
          alt="Riser Lines"
          title="Riser Lines"
          v-on:click="got_clicked_rla"
        />
        <img
          src="../assets/icon/brake.png"
          alt="Brake Lines"
          title="Brake Lines"
          v-on:click="got_clicked_brake_lines"
        />
      </span>
      <button type="button" class="btn d-block d-lg-none" v-on:click="run_the_software">
        <i class="fas fa-play sidebar_icons"></i>
        <b class="d-none">Run</b>
      </button>

      <!-- Sidebar pagination which later discarded
      <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" 
      data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" 
      aria-label="Toggle navigation" v-on:click="topbar_flag = !topbar_flag">
        <i class="fas fa-align-justify"></i>
      </button>
      -->
      <div
        class="navbar-collapse"
        id="navbarSupportedContent"
        v-bind:class="{collapse: topbar_flag}"
      >
        <ul class="nav navbar-nav ml-auto" style="float: right;">
          <li class="nav-item" v-on:click="got_clicked_planform">
            <img
              src="../assets/icon/planform.png"
              alt="Planform"
              title="Planform"
              height="40"
              width="40"
            />
          </li>
          <li class="nav-item" v-on:click="got_clicked_airfoil">
            <img
              src="../assets/icon/airfoil.png"
              alt="Airfoil"
              title="Airfoil"
              height="40"
              width="40"
            />
          </li>
          <li class="nav-item" v-on:click="got_clicked_volute">
            <img src="../assets/icon/volute.png" alt="Volute" title="Volute" height="40" width="40" />
          </li>
          <li class="nav-item" v-on:click="got_clicked_al">
            <img src="../assets/icon/anchor.png" alt="Anchor" title="Anchor" height="40" width="40" />
          </li>
          <li class="nav-item" v-on:click="got_clicked_fp">
            <img src="../assets/icon/panels.png" alt="Panels" title="Panels" height="40" width="40" />
          </li>
          <li class="nav-item" v-on:click="got_clicked_rla">
            <img
              src="../assets/icon/riserlines.png"
              alt="Riser Lines"
              title="Riser Lines"
              height="40"
              width="40"
            />
          </li>
          <li class="nav-item" v-on:click="got_clicked_brake_lines">
            <img
              src="../assets/icon/brake.png"
              alt="Brake Lines"
              title="Brake Lines"
              height="40"
              width="40"
            />
          </li>
          <li class="nav-item" v-on:click="run_the_software">
            <img src="../assets/icon/run.png" alt="Run" title="Run" height="40" width="40" />
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { EventBus } from "../main.js";
import { collect_inputs } from "../save_inputs.js";
export default {
  data: function() {
    return {
      topbar_flag: true,
      sidebar_collapse_flag: false,
      solver_result: {},
    };
  },
  methods: {
    got_clicked: function() {
      document.getElementsByClassName("small_screen_overlay")[0].style.display = "block";
      this.sidebar_collapse_flag = !this.sidebar_collapse_flag;
      EventBus.$emit("sidebar_flag_got_clicked", this.sidebar_collapse_flag);
    },
    got_clicked_planform: function() {
      EventBus.$emit(
        "input_param_planform_got_clicked",
        this.input_param_planform_flag
      );
    },
    got_clicked_airfoil: function() {
      EventBus.$emit(
        "input_param_airfoil_got_clicked",
        this.input_param_airfoil_flag
      );
    },
    got_clicked_volute: function() {
      EventBus.$emit(
        "input_param_volute_got_clicked",
        this.input_param_volute_flag
      );
    },
    got_clicked_al: function() {
      EventBus.$emit("input_param_al_got_clicked", this.input_param_al_flag);
    },
    got_clicked_fp: function() {
      EventBus.$emit("input_param_fp_got_clicked", this.input_param_fp_flag);
    },
    got_clicked_rla: function() {
      EventBus.$emit("input_param_rla_got_clicked", this.input_param_rla_flag);
    },
    got_clicked_brake_lines: function() {
      EventBus.$emit(
        "input_param_brake_lines_got_clicked",
        this.input_param_brake_lines_flag
      );
    },

    create_request: function() {
      let inp = collect_inputs();
      this.axios.post("/api/submit", inp).then(res => {
        Object.assign(this.solver_result, res.data);
        EventBus.$emit("solver_overall_result", this.solver_result);
      });
    },

    run_the_software: function() {
      if (
        document.getElementById("softwareOutput").children[1].children.length
      ) {
        document
          .getElementById("softwareOutput")
          .removeChild(
            document
              .getElementById("softwareOutput")
              .getElementsByTagName("div")[1]
          );
        let a = document.createElement("div");
        a.setAttribute("class", "content");
        document
          .getElementById("softwareOutput")
          .insertBefore(
            a,
            document.getElementById("softwareOutput").lastChild
          );
      }
      document.getElementById("loader").style.display = "block";
      document.getElementById("softwareOutput").style.backgroundImage =
        "url('')";
      document.getElementById("softwareOutput").style.backgroundColor =
        "#1c2020";
      document.getElementsByClassName("welcome_div")[0].style.display = "none";
      this.create_request();
    }
  },
  created() {
    EventBus.$on("sidebar_run_got_clicked", run_flag => {
      if (run_flag) {
        this.run_the_software();
      }
    });
    EventBus.$on("mobile_sidebar_toggle", sidebar_toggle => {
      this.sidebar_collapse_flag = sidebar_toggle;
    });
    EventBus.$on("android_swipe_toggle", swipe => {
      this.sidebar_collapse_flag = !swipe;
    });
  }
};
</script>