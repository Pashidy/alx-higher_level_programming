$(document).ready(function() {
    // Fetch data from the URL
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        // Extract movie titles from the fetched data
        const movies = data.results;

        // Iterate over each movie and add its title to the list
        movies.forEach(function(movie) {
            // Create a new list item with the movie title
            const listItem = $('<li>').text(movie.title);

            // Append the list item to the UL#list_movies
            $('ul#list_movies').append(listItem);
        });
    });
});
