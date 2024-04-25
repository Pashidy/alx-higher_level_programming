#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  try {
    const movie = JSON.parse(body);
    console.log(`Characters of ${movie.title}:`);
    movie.characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Failed to fetch data. Status code:', response.statusCode);
          return;
        }

        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
