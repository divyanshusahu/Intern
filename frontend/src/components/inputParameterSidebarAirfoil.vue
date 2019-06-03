<template>
    
    <div class="custom_modal" id="airfoil_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <!--<div class="input_popup">
            <div class="custom_modal_header">
                <h6>Airfoil Input</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tr>
                        <td>Chord length Percentage</td>
                        <td><input type="number" value="5" name="airfoil_clp" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Angle with chord length (deg)</td>
                        <td><input type="number" value="45" name="airfoil_acl" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Standard Airfoil</td>
                        <td>
                            <select name="standard_airfoil">
                                <option value="ClarkY">ClarkY</option>
                                <option value="NACA 0012">NACA 0012</option>
                                <option value="NACA 0009">NACA 0009</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Or from file</td>
                        <td></td>
                    </tr>
                </table>
            </div>
            <div class="custom_modal_footer">
                <button type="button" class="input_close_button" v-on:click="input_toggle =! input_toggle">Close</button>
            </div>
        </div>-->
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Airfoil Input<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <table class="table table-borderless">
                    <tr>
                        <td>Chord length Percentage</td>
                        <td><input type="number" value="5.0" name="airfoil_clp" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Angle with chord length (deg)</td>
                        <td><input type="number" value="135.0" name="airfoil_acl" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Standard Airfoil</td>
                        <td>
                            <select name="standard_airfoil">
                                <option value="ClarkY">ClarkY</option>
                                <option value="NACA 0012">NACA 0012</option>
                                <option value="NACA 0009">NACA 0009</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <!--<td>Or from file</td>-->
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
            input_toggle : true,
            airfoil_input_obj : {}
        }
    },
    created() {
        EventBus.$on('input_param_airfoil_got_clicked', (input_param_airfoil_flag) => {
            this.input_toggle = input_param_airfoil_flag;
        });

        EventBus.$on('run_got_clicked', (run_clicked_flag) => {
            if (run_clicked_flag)
            {
                this.airfoil_input_obj["rib_description"] = {
                    "LE_cut" : {
                        "angle_with_chord_line" : document.getElementsByName("airfoil_acl")[0].value,
                        "chord_length_percentc" : document.getElementsByName("airfoil_clp")[0].value
                    },
                    "aerofoil" : "../solverMain/test/airfoil.txt",
                    "lightening_holes": [
                        {
                            "shape": "ELLIPTIC", 
                            "box_index": 0, 
                            "minor_to_major_axes": 0.7, 
                            "size": 5
                        }, 
                        {
                            "shape": "TRIANGULAR", 
                            "box_index": 1, 
                            "minor_to_major_axes": 0.7
                        }
                    ],
                };
                EventBus.$emit('inputParamAI_obj', this.airfoil_input_obj);
            }
        });
    }
}
</script>

