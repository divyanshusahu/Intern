<template>
    <div id="outputLog" class="card">
        <p>{{ result }}</p>
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
            console.log(this.result)
        });
    }
}
</script>

