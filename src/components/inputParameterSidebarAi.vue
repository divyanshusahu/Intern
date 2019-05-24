<template>
    
    <div class="custom_modal" id="advance_input_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <div class="input_popup">
            <div class="custom_modal_header">
                <h6>Advance Input</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tr>
                        <td><b>Transform Geometry</b></td>
                        <td></td>
                        <td><b>Slider</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Rotation Axis(x,y,z)</td>
                        <td><input type="text" value="0,0,0" name="advip_tg_ra" style="width: 100px"></td>
                        <td>Area Percentage</td>
                        <td><input type="number" value="2" name="advip_slider_ap" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Translation Axix(x,y,z)</td>
                        <td><input type="text" value="0,0,0" name="advip_tg_ta" style="width: 100px"></td>
                        <td>Width Length Ratio</td>
                        <td><input type="number" value="0.5" name="advip_slider_wlr" style="width: 100px"></td>
                    </tr>

                </table>
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
    data : function() {
        return {
            input_toggle : true
        }
    },
    created() {
        EventBus.$on("input_param_ai_got_clicked", (input_param_ai_flag) => {
            this.input_toggle = input_param_ai_flag;
        });
    }
}
</script>
