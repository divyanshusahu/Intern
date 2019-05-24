<template>
    
    <div class="custom_modal" id="anchor_location_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <div class="input_popup">
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

        </div>
    </div>

</template>

<script>
import { EventBus } from '../main.js';
export default {
    data : function(){
        return {
            input_toggle : true
        }
    },
    created() {
        EventBus.$on("input_param_al_got_clicked", (input_param_al_flag) => {
            this.input_toggle = input_param_al_flag;
        });
    }
}
</script>

