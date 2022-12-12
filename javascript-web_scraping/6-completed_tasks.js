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
    let c = 0;
    for (const i of mydata) {
      c += 1;
      let idcom = i['userId'];
      if ((c === i['userId']) && (i['completed'] === true)) {
        counter += 1;
        mydict[idcom] = counter;
      }
    }
    console.log(mydict);
  }
});
