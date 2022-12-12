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
    let c = 1;
    for (const i of mydata) {
      let idcom = i['userId'];
      if ((idcom === i['userId']) && (i['completed'] === true)) {
        counter += 1;
        mydict[idcom] = counter;
      }
      c += 1;
    }
    console.log(mydict);
    console.log(c);
  }
});
