<template>
    
    <div class="custom_modal" id="planform_modal" 
    v-bind:class="{pop_up_toggle : input_toggle}">
        <!--<div class="input_popup">
            <div class="custom_modal_header">
                <h6>Planform Input</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tr>
                        <td>Total Ribs</td>
                        <td><input type="number" value="28" name="planform_total_ribs" style="width: 100px"></td>
                        <td>Platform Type</td>
                        <td>
                            <select name="planform_plftype">
                                <option value="rectangular">Rectangular</option>
                                <option value="elliptical">Elliptical</option>
                                <option value="user-define">User Define</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Span(mm)</td>
                        <td><input type="number" value="16180" name="planform_span" style="width: 100px"></td>
                        <td>Chord(mm)</td>
                        <td><input type="number" value="5810" name="planform_chrod" style="width: 100px"></td>
                    </tr>
                </table>
            </div>
            <div class="custom_modal_footer">
                <button type="button" class="input_close_button" v-on:click="input_toggle = !input_toggle">Close</button>
            </div>

        </div>-->
        <div class="card bg-light input_popup">
            <div class="card-header">
                <h5>Planform Input<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <form id="planform_input_form">
                <table class="table table-borderless">
                    <tr>
                        <td>Total Ribs</td>
                        <td><input type="number" value="28.0" name="planform_total_ribs" style="width: 100px"></td>
                        <td>Platform Type</td>
                        <td>
                            <select name="planform_plftype">
                                <option value="RECTANGULAR">Rectangular</option>
                                <option value="ELLIPTICAL">Elliptical</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Span(mm)</td>
                        <td><input type="number" value="16180.0" name="planform_span" style="width: 100px"></td>
                        <td>Chord(mm)</td>
                        <td><input type="number" value="5810.0" name="planform_chord" style="width: 100px"></td>
                    </tr>
                </table>
                </form>
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
            input_toggle : true,
            planform_input_obj : {}
        }
    },
    created() {
        EventBus.$on('input_param_planform_got_clicked', (input_param_planform_flag) => {
            this.input_toggle = input_param_planform_flag;
        });

        EventBus.$on('run_got_clicked', (run_clicked_flag) => {
            if (run_clicked_flag)
            {
                this.planform_input_obj["planform_description"] = {
                    "max_chord_length" : parseFloat(document.getElementsByName("planform_chord")[0].value).toFixed(1),
                    "spanwise_chord_length_percentc": [
                        [
                            0, 
                            0, 
                            100
                        ], 
                        [
                            10, 
                            0, 
                            100
                        ], 
                        [
                            30, 
                            2, 
                            96
                        ], 
                        [
                            50, 
                            5, 
                            90
                        ], 
                        [
                            70, 
                            10, 
                            80
                        ], 
                        [
                            100, 
                            18, 
                            64
                        ]
                    ],
                    "shape" : document.getElementsByName("planform_plftype")[0].value,
                    "span_length" : parseFloat(document.getElementsByName("planform_span")[0].value).toFixed(1),
                };

                this.planform_input_obj["number_of_panel"] = parseFloat(document.getElementsByName("planform_total_ribs")[0].value);
                EventBus.$emit('inputParamPLANFORM_obj', this.planform_input_obj);
            }
        });
    }
}
</script>

