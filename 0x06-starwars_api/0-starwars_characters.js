#!/bin/usr/node
// Interview Challenge Starwars Characters


// Store command line arguments in `args` variable
const args = process.argv;

// Define URL for SWAPI (Star Wars API) films
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Create a new URL by appending the film ID from the command line arguments
const movieUrl = `${filmUrl}${args[2]}/`;

// Require 'request' module for making HTTP requests
const request = require('request');

// Function to make requests to the character URLs
function charRequest (idx, url, characters, limit) {
  // If idx is equal to limit, all characters have been printed and function can return
  if (idx === limit) {
    return;
  }
  
  // Make HTTP request to the character URL
  request(url, function (error, response, body) {
    if (!error) {
      // Parse JSON data received from request
      const rbody = JSON.parse(body);
      // Print name of character to console
      console.log(rbody.name);
      // Increment idx value and make recursive call to CharRequest with new index
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
    // Parse JSON data received from request
    const fbody = JSON.parse(body);
    // Retrieve array of character URLs from data
    const characters = fbody.characters;
    if (characters && characters.length > 0) {
      // Get length of array and call CharRequest function with initial parameters
      const limit = characters.length;
      charRequest(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});
