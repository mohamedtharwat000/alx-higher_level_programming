#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const wedgeAntillesMovies = data.results.filter((movie) =>
      movie.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/'
      )
    );
    console.log(wedgeAntillesMovies.length);
  }
});
