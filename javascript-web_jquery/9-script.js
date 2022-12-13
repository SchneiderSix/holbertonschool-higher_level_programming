#!/usr/bin/node
fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
    .then(result => result.json())
    .then((output) => {
        document.getElementById('hello').innerHTML = output.hello;
}).catch(err => console.error(err));
