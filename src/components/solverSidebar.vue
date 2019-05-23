<template>
	<li>
  	<a href="#" data-toggle="collapse" aria-expended="false" class="dropdown-toggle"
		v-on:click="solver_flag = !solver_flag">Solver</a>
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
export default {
	data : function() {
		return {
			solver_flag : true
		};
	}
}
</script>
