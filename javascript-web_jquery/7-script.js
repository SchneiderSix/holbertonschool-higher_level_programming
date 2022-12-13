#!/usr/bin/node
fetch('https://swapi-api.alx-tools.com/api/people/5')
    .then(result => result.json())
    .then((output) => {
        document.getElementById('character').innerHTML = output.name;
        
}).catch(err => console.error(err));
