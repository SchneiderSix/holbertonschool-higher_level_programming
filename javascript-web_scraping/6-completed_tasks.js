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
    let flag = false;
    for (const i of mydata) {
      let idcom = i['userId'];
      if ((idcom === i['userId']) && (i['completed'] === true)) {
        if ((flag === true) && (!mydict[idcom])) {
          counter = 0;
        }
        counter += 1;
        mydict[idcom] = counter;
        flag = true;
      }
    }
    console.log(mydict);
  }
});
