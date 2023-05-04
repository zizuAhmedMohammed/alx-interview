#!/usr/bin/node
const args = process.argv;
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieUrl = `${filmUrl}${args[2]}/`;

// Require 'request' module for making HTTP requests
const request = require('request');

// Function to make requests to the character URLs
function charRequest (idx, url, characters, limit) {
  if (idx === limit) {
    return;
  }
  
  // Make HTTP request to the character URL
  request(url, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      idx++;
      charRequest(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}

// Main function
request(movieUrl, function (error, response, body) {
  if (error == null) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;
    if (characters && characters.length > 0) {
      const limit = characters.length;
      charRequest(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});
