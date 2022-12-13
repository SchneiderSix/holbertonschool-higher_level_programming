#!/usr/bin/node
$(document).ready(function()
{
    $('#update_header').click(function() {
        const tx = $("header").text().replace("First HTML page", "New Header!!!");
        $("header").text(tx);
    });
});
