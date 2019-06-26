<template>
    
    <div class="custom_modal" id="anchor_location_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <!--<div class="input_popup">
            <div class="custom_modal_header">
                <h6>Anchor Description</h6>
            </div>
            <div class="custom_modal_content">
                <b>Ribs Connection</b>
                <select name="ribs_connection">
                    <option value="all_ribs">All Ribs</option>
                    <option value="alternative_ribs">Alternative Ribs</option>
                    <option value="User_defined">User Defined</option>
                </select>
            </div>
            <div class="custom_modal_footer">
                <button type="button" class="input_close_button"
                v-on:click="input_toggle = !input_toggle">Close</button>
            </div>
        </div>-->
       
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Anchor Description<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <label>Ribs Connection</label>
                <select name="ribs_connection">
                    <option value="ALL">All Ribs</option>
                    <option value="ALTERNATE">Alternative Ribs</option>
                </select>
            </div>
            <div class="card-footer">
                <button type="button" class="btn btn-success" v-on:click="input_toggle = !input_toggle">Close</button>
            </div>
        </div>
    </div>

</template>

<script>
import { EventBus } from '../main.js';
export default {
    data : function(){
        return {
            input_toggle : true,
            anchor_loation_value : null
        }
    },
    created() {
        EventBus.$on("input_param_al_got_clicked", (input_param_al_flag) => {
            this.input_toggle = input_param_al_flag;
        });

        EventBus.$on('run_got_clicked', (run_clicked_flag) => {
            if (run_clicked_flag)
            {
                this.anchor_loation_value = document.getElementsByName("ribs_connection")[0].value;
                EventBus.$emit('inputParamAL_obj', this.anchor_loation_value);
            }
        })
    }
}
</script>

