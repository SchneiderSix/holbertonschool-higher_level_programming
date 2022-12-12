#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    let mydict = {};
    let counter = 0;
    let idcom = 1;
    for (const i of mydata) {
      if ((i['userId'] === idcom) && (i['completed'] === true)) {
        counter += 1;
        mydict[idcom] = counter;
      }
      idcom += 1;
    }
    console.log(mydict);
  }
});
