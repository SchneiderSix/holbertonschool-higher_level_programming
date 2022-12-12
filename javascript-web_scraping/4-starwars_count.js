#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    let c = 0;
    for (const i in mydata.results) {
      for (const j in i.characters) {
        if (j.endsWith('/18/')) {
          c += 1;
        }
      }
    }
    console.log(c);
  }
});
