#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    let mydict = {};
    for (const i of mydata) {
      let idcom = i['userId'];
      let counter = 0;
      if (i['userId'] === idcom) {
        if (i['completed'] === true) {
          counter += 1;
          mydict[userId] = counter;
        }
      }
    }
    console.log(mydict);
  }
});
