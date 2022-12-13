#!/usr/bin/node
$(document).ready(function()
{
    $("#toggle_header").click(function() {
        $("header").removeClass("green");
        $("header").addClass("red");
    });
});
