#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    const mydict = {};
    let counter = 0;
    for (const i of mydata) {
      const idcom = i.userId;
      if (i.completed === true) {
        mydict[idcom] = '';
        if (mydict[idcom]) {
          counter += 1;
          mydict[idcom] = counter;
        } else {
          counter = 0;
        }
      }
    }
    console.log(mydict);
  }
});
