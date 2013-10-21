$(document).ready(function() {
    var popin = $('.mail-form').jqPopin(
        {trigger: $(".share .mail"),
         close: $(".close_popin")}
    );
    $("#frameId").height($("#frameId").contents().find("html").height());

    $(".share > span").toggle(
        function() {
            $(this).next("table").show();
        },
        function() {
            $(this).next("table").hide();
        }
    );
});