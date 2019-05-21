$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');

    });

    $("#btn_round_canopy").on('click', function() {
        $("#round_canopy_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_planform").on('click', function() {
        $("#planform_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_airfoil").on('click', function() {
        $("#airfoil_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_volute").on('click', function() {
        $("#volute_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_anchor_location").on('click', function() {
        $("#anchor_location_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_flat_panels").on('click', function() {
        $("#flat_panels_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_rigging_lines_arrangement").on('click', function() {
        $("#rigging_lines_arrangement_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_brake_lines").on('click', function() {
        $("#brake_lines_modal").toggleClass("pop_up_toggle");
    });

    $("#btn_advance_input").on('click', function() {
        $("#advance_input_modal").toggleClass("pop_up_toggle");
    });

    $(".input_close_button").on("click", function() {
        $(".custom_modal").addClass("pop_up_toggle");
    })
});