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
      const idcom = i["userId"];
      if ((idcom === i["userId"]) && (i["completed"] === true)) {
        if (!mydict[idcom]) {
          counter = 0;
        }
        counter += 1;
        mydict[idcom] = counter;
      }
    }
    console.log(mydict);
  }
});
