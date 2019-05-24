<template>
    
    <div class="custom_modal" id="flat_panels_modal"
    v-bind:class="{pop_up_toggle : input_toggle}">
        <div class="input_popup">
            <div class="custom_modal_header">
                <h6>Flat panels</h6>
            </div>
            <div class="custom_modal_content">
                <table class="table table-borderless">
                    <tr>
                        <td><b>Sewing Allowances</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Max Value(mm)</td>
                        <td><input type="number" value="50" name="flat_panels_sa_max_value" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Min Value(mm)</td>
                        <td><input type="number" value="1" name="flat_panels_sa_min_value" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td><b>Sewing Allowance for Ribs</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Sides (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_sar_sides" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Front (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_sar_front" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Rear (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_sar_rear" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td><b>Sewing Allowance Panel</b></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Sides (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_swp_sides" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Front (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_swp_front" style="width: 100px"></td>
                    </tr>
                    <tr>
                        <td>Rear (% of chord)</td>
                        <td><input type="number" value="2" name="flat_panels_swp_rear" style="width: 100px"></td>
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
        EventBus.$on("input_param_fp_got_clicked", (input_param_fp_flag) => {
            this.input_toggle = input_param_fp_flag;
        });
    }
}
</script>
