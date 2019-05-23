<template>
  <li>
        <a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle" 
        v-on:click="view_flag = !view_flag">
        <i class="fas fa-eye"></i>View</a>
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
export default {
  data : function() {
    return {
      view_flag: true
    };
  }
}
</script>
