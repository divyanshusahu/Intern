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
                        <td><input type="text" value="1.0,35.0,75.0,90.0" name="rla_cl_location" style="width: 100%"></td>
                    </tr>
                    <tr>
                        <td>Suspension Length(mm)</td>
                        <td><input type="number" value="6800.0" name="rla_cl_susplen" style="width: 100%"></td>
                    </tr>
                    <tr>
                        <td>Distance between Karabiners Length</td>
                        <td><input type="number" value="400.0" name="advip_others_dkl" style="width: 100px"></td>
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
            input_toggle : true,
            rla_obj : {},
            al_value : null
        }
    },
    created() {
        EventBus.$on('input_param_rla_got_clicked', (input_param_rla_flag) => {
            this.input_toggle = input_param_rla_flag;
        });

        EventBus.$on("inputParamAL_obj", (anchor_location_value) => {
            this.al_value = anchor_location_value;
        });

        EventBus.$on('run_got_clicked', (run_clicked_flag) => {
            if (run_clicked_flag)
            {
                this.rla_obj["anchor_description"] = [
                    {
                        "L1_combination" : [
                            [
                                0,
                                1
                            ],
                            [
                                2,
                                3
                            ]
                        ],
                        "rib_connection" : this.al_value,
                        "riser_length" : parseFloat(document.getElementsByName("rla_cl_susplen")[0].value).toFixed(1),
                        "chordwise_locations_percentc" : document.getElementsByName("rla_cl_location")[0].value.split(",").map(
                            function(x) {
                                return parseFloat(x,10).toFixed(1);
                            }
                        ),
                        "distance_between_karabinas" : parseFloat(document.getElementsByName("advip_others_dkl")[0].value).toFixed(1),
                        "L1_length_percentl": 20.0, 
                        "user_defined_ribs": [
                            0, 
                            3, 
                            8, 
                            13
                        ],
                        "riser_end_separation_length": 400.0,
                    }
                ];
                EventBus.$emit('inputParamRLA_obj', this.rla_obj);
            }
        });
    }
}
</script>