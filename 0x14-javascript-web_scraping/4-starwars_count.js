#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles' character ID

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
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log('Number of movies with Wedge Antilles:', moviesWithWedgeAntilles.length);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
