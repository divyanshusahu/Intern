<template>
    
    <div class="custom_modal" id="rigging_lines_arrangment_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Rigging Lines Arrangment<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <table class="table table-borderless">
                    <tr>
                        <td><b>Chordwise Location</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Location(% of chord)</td>
                        <td><input type="text" value="1,35,75,90" name="rla_cl_location" style="width: 100%"></td>
                    </tr>
                    <tr>
                        <td>Suspension Length(mm)</td>
                        <td><input type="number" value="6800" name="rla_cl_susplen" style="width: 100%"></td>
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
        EventBus.$on('input_param_rla_got_clicked', (input_param_rla_flag) => {
            this.input_toggle = input_param_rla_flag;
        });
    }
}
</script>