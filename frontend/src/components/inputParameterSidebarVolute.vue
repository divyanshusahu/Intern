<template>
    
    <div class="custom_modal" id="volute_modal"
    v-bind:class="{pop_up_toggle: input_toggle}">
        <!--<div class="input_popup">
            <div class="custom_modal_header">
                <h6>Volute Input</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tr>
                        <td>Shape</td>
                        <td>Elleptic</td>
                    </tr>
                    <tr>
                        <td>Minot to major axis ratio</td>
                        <td><input type="number" value="1" name="volute_input_minot_ratio" stylr="width:100px;"></td>
                    </tr>
                    <tr>
                        <td>Semi Span Angle(deg)</td>
                        <td><input type="number" value="45" name="volute_input_ssa" style="width: 100px"></td>
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
                <h5>Volute Input<span v-on:click="input_toggle = !input_toggle">&times;</span></h5>
            </div>
            <div class="card-body">
                <table class="table table-borderless">
                    <tr>
                        <td>Shape</td>
                        <td>Elliptic</td>
                    </tr>
                    <tr>
                        <td>Minot to major axis ratio</td>
                        <td><input type="number" value="1.0" name="volute_input_minot_ratio" stylr="width:100px;"></td>
                    </tr>
                    <tr>
                        <td>Semi Span Angle(deg)</td>
                        <td><input type="number" value="45.0" name="volute_input_ssa" style="width: 100px"></td>
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
            volute_obj : {}
        }
    },
    created() {
        EventBus.$on("input_param_volute_got_clicked", (input_param_volute_flag) => {
            this.input_toggle = input_param_volute_flag;
        });

        EventBus.$on("run_got_clicked", (run_clicked_flag) => {
            if (run_clicked_flag)
            {
                this.volute_obj["volute_description"] = {
                    "shape" : "ELLIPTIC",
                    "semi_span_angle" : document.getElementsByName("volute_input_ssa")[0].value,
                    "minor_to_major_axes" : document.getElementsByName("volute_input_minot_ratio")[0].value
                };
                EventBus.$emit('inputParamVOLUTE_obj', this.volute_obj);
            }
        });
    }
}
</script>

