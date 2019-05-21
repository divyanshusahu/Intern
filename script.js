$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');

    });

    $("#btn_round_canopy").on('click', function() {
        $("#round_canopy_modal").toggleClass("pop_up_toggle");
        //$("#input_round_canopy").toggleClass("pop_up_toggle");
    });

    /*$(".input_close_button").on("click", function() {
        $(".custom_modal").toggleClass("pop_up_toggle");
    })*/
});