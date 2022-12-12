#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const mydata = JSON.parse(body);
    const mydict = {};
    for (const i of mydata) {
      if (i.completed === true) {
        if (i.userId in mydict) {
          mydict[i.userId]++;
        } else {
          mydict[i.userId] = 1;
        }
      }
    }
    console.log(mydict);
  }
});
