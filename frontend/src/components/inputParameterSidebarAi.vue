<template>
    
    <div class="custom_modal" id="advance_input_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <!--<div class="input_popup">
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
        </div>-->
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Advance Input<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
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
                    <tr>
                        <td><b>Washout Description</b></td>
                        <td></td>
                        <td><b>Side Flap Description</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Tip Angle(deg)</td>
                        <td><input type="number" value="0" name="advip_washout_description_ta" style="width: 100px"></td>
                        <td>Rear Edge Length</td>
                        <td><input type="number" value="10" name="advip_sfd_rel" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Center of Rotation</td>
                        <td><input type="number" value="0" name="advip_washout_description_cr" style="width: 100px"></td>
                        <td>Front Edge Length</td>
                        <td><input type="number" value="20" name="advip_sfd_fel" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Variation</td>
                        <td>
                            <select name="advip_washout_description_variation">
                                <option value="Quadratic">Quadratic</option>
                                <option value="Linear">Linear</option>
                            </select>
                        </td>
                        <td>Index</td>
                        <td><input type="number" value="0" name="advip_sfd_index" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td><b>Others</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Distance Karabiners Length</td>
                        <td><input type="number" value="400" name="advip_others_dkl" style="width: 100px"></td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Mesh Size</td>
                        <td><input type="number" value="3" name="advip_others_ms" style="width: 100px"></td>
                        <td></td>
                        <td></td>
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
