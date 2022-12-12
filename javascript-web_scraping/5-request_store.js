#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
    console.log('statusCode:', response.statusCode);
  } else {
    const thingstosave = JSON.parse(body);
    fs.writeFile(process.argv[3], thingstosave, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
