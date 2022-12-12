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
      if (i['completed'] === true) {
        mydict.push({
          key: i['userId'],
          value: i['id']
        });
      }
    }
    console.log(mydict);
  }
});
