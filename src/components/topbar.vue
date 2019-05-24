<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <button type="button" id="sidebarCollapse" class="navbar-btn">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" 
      data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" 
      aria-label="Toggle navigation" v-on:click="topbar_flag = !topbar_flag">
        <i class="fas fa-align-justify"></i>
      </button>

      <div class="navbar-collapse" id="navbarSupportedContent" v-bind:class="{collapse: topbar_flag}">
        <ul class="nav navbar-nav ml-auto" style="float: right;">
          <li class="nav-item">
            <a class="nav-link" href="#">Com 1</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 2</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 3</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 4</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Com 5</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Run</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data : function() {
    return {
      topbar_flag : true,
    };
  }
}
</script>
