#!/usr/bin/node
$(document).ready(function()
{
    function Get(yourUrl){
        var Httpreq = new XMLHttpRequest(); // a new request
        Httpreq.open("GET",yourUrl,false);
        Httpreq.send(null);
        return Httpreq.responseText;          
    }
    var mydata = JSON.parse(Get('https://swapi-api.hbtn.io/api/people/5/?format=json'));
    const mychar = document.getElementById('character');
    mychar.innerHTML = "mydata";
});
