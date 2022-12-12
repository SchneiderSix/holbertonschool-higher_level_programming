#!/usr/bin/node
const request = require('request');
request('http://www.google.com', function (error, response) {
  console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
