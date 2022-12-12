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
      if (mydata[i]['completed'] === true) {
        mydict.push({
          key: mydata[i]['userId'],
          value: mydata[i]['id']
        });
      }
    }
    console.log(mydict);
  }
});
