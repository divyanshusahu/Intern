<template>
    
    <div class="custom_modal" id="brake_lines_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Brake Lines<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <table class="table table-borderless">
                    <tr>
                        <td>Brake Ribs</td>
                        <td><input type="text" value="2,5,7,10" name="bl_brake_ribs" style="width: 100%"></td>
                    </tr>
                </table>
            </div>
            <div class="card-footer">
                <button type="button" class="btn btn-success" v-on:click="input_toggle = !input_toggle">Close</button>
            </div>
        </div>
    </div>

</template>

<script>
import { EventBus } from '../main.js'

export default {
    data : function() {
        return {
            input_toggle : true
        }
    },
    created() {
        EventBus.$on('input_param_brake_lines_got_clicked', (input_param_brake_lines_flag) => {
            this.input_toggle = input_param_brake_lines_flag;
        });
    }
}
</script>