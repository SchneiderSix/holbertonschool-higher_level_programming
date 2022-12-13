#!/usr/bin/node
fetch('https://swapi-api.alx-tools.com/api/films')
    .then(result => result.json())
    .then((output) => {
        const fragment = document.createDocumentFragment();
        for (const i of output.results) {
                const tit = i.title;
                let li = document.createElement('li');
                li.textContent = tit;
                fragment.appendChild(li);
        }
        const myul = document.getElementById('list_movies');
        myul.appendChild(fragment);

}).catch(err => console.error(err));
