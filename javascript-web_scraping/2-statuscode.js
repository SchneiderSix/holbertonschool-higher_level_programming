#!/usr/bin/node
const request = require('request');
request('http://www.google.com', function (response) {
  console.log('code:', response && response.statusCode);
});
