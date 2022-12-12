#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    if (response.statusCode === 200) {
      const all_data = JSON.parse(body);
      let c = 0;
      for (const i in all_data.results()) {
        for (const j in i.characters)
          if (j === 'https://swapi-api.hbtn.io/api/people/18/') {
            c += 1;
          }
      }
      console.log(c);
    }
  }
});
