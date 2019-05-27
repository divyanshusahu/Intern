<template>
    
    <div class="custom_modal" id="round_canopy_modal" 
    v-bind:class="{pop_up_toggle: input_toggle}">
        <!--<div class="input_popup">
            <div class="custom_modal_header">
                <h6>Round Parachute</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tbody>
                        <tr>
                            <td><b>Round Parachute</b></td>
                            <td></td>
                            <td><b>Sewing Allowances</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>No. of Panels</td>
                            <td><input type="number" value="20" name="round_canopy_n_panels" style="width:100px;"></td>
                            <td>Max value</td>
                            <td><input type="number" value="50" name="sewing_allowances_max" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>No. of Suspension Lines</td>
                            <td><input type="number" value="9" name="round_canopy_n_susplines" style="width:100px;"></td>
                            <td>Min value</td>
                            <td><input type="number" value="1" name="sewing_allowances_min" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>No. of Slot</td>
                            <td><input type="number" value="6" name="round_canopy_n_slot" style="width:100px;"></td>
                            <td>Panel Side</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_ps" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>External diameter</td>
                            <td><input type="number" value="10000" name="round_canopy_exdia" style="width:100px;"></td>
                            <td>Panel Front</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_pf" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Ring Diameter</td>
                            <td><input type="number" value="1000" name="round_canopy_ringdia" style="width:100px;"></td>
                            <td>Panel Rear</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_pr" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Slot Width</td>
                            <td><input type="number" value="100" name="round_canopy_sw" style="width:100px;"></td>
                            <td><b>Transformation Geometry</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>Suspension Length</td>
                            <td><input type="number" value="1000" name="round_canopy_susplen" style="width:100px;"></td>
                            <td>Rotation Angle</td>
                            <td><input type="text" value="0,0,0" name="tg_ra" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Conical height</td>
                            <td><input type="number" value="0" name="round_canopy_conhg" style="width:100px;"></td>
                            <td>Translation</td>
                            <td><input type="text" value="0,0,0" name="tg_translation" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Skirt Width</td>
                            <td><input type="number" value="0" name="round_canopy_skwdt" style="width:100px;"></td>
                            <td><b>Mesh Parameter</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td>Edge Length</td>
                            <td><input type="number" value="2" name="mesh_param_el" style="width:100px;"></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="custom_modal_footer">
                <button type="button" class="input_close_button" v-on:click="input_toggle = !input_toggle">Close</button>
            </div>
        </div>-->
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Round Parachute<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <table class="table table-borderless">
                    <tbody>
                        <tr>
                            <td><b>Round Parachute</b></td>
                            <td></td>
                            <td><b>Sewing Allowances</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>No. of Panels</td>
                            <td><input type="number" value="20" name="round_canopy_n_panels" style="width:100px;"></td>
                            <td>Max value</td>
                            <td><input type="number" value="50" name="sewing_allowances_max" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>No. of Suspension Lines</td>
                            <td><input type="number" value="9" name="round_canopy_n_susplines" style="width:100px;"></td>
                            <td>Min value</td>
                            <td><input type="number" value="1" name="sewing_allowances_min" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>No. of Slot</td>
                            <td><input type="number" value="6" name="round_canopy_n_slot" style="width:100px;"></td>
                            <td>Panel Side</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_ps" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>External diameter</td>
                            <td><input type="number" value="10000" name="round_canopy_exdia" style="width:100px;"></td>
                            <td>Panel Front</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_pf" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Ring Diameter</td>
                            <td><input type="number" value="1000" name="round_canopy_ringdia" style="width:100px;"></td>
                            <td>Panel Rear</td>
                            <td><input type="number" value="0.5" name="sewing_allowances_pr" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Slot Width</td>
                            <td><input type="number" value="100" name="round_canopy_sw" style="width:100px;"></td>
                            <td><b>Transformation Geometry</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td>Suspension Length</td>
                            <td><input type="number" value="1000" name="round_canopy_susplen" style="width:100px;"></td>
                            <td>Rotation Angle</td>
                            <td><input type="text" value="0,0,0" name="tg_ra" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Conical height</td>
                            <td><input type="number" value="0" name="round_canopy_conhg" style="width:100px;"></td>
                            <td>Translation</td>
                            <td><input type="text" value="0,0,0" name="tg_translation" style="width:100px;"></td>
                        </tr>
                        <tr>
                            <td>Skirt Width</td>
                            <td><input type="number" value="0" name="round_canopy_skwdt" style="width:100px;"></td>
                            <td><b>Mesh Parameter</b></td>
                            <td></td>
                        </tr>
                        <tr>
                            <td></td>
                            <td></td>
                            <td>Edge Length</td>
                            <td><input type="number" value="2" name="mesh_param_el" style="width:100px;"></td>
                        </tr>
                    </tbody>
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
        EventBus.$on('rc_input_param_got_clicked', (rc_input_param_flag) => {
            this.input_toggle = rc_input_param_flag;
        });
    }
}
</script>
