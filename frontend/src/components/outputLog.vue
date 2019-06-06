<template>
    <div id="outputLog" class="card">
        <!--<p>{{ result.input_file }}</p>
        <p>{{ result.input_file_result }}</p>
        <p>{{ result.running_solver }}</p>
        <p>{{ result.running_solver_result}}</p>
        <p>{{ result.running_gmsh }}</p>
        <p>{{ result.running_gmsh_result }}</p>
        <p>{{ result.converting_vtp }}</p>
        <p>{{ result.coverting_vtp_result }}</p>
        <p>{{ result.success }}</p>-->
        <p>{{ this.result }}</p>
    </div>
</template>

<script>
import { EventBus } from '../main.js';
export default {
    data : function() {
        return {
            result : {}
        }
    },
    created() {
        EventBus.$on("solver_overall_result",(solver_result) =>{
            Object.assign(this.result, solver_result);
            this.$forceUpdate();
        });
    }
}
</script>

