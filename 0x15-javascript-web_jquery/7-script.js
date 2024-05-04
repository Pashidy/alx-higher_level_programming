$(document).ready(function() {
    // Fetch data from the URL
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
        // Extract the character name from the fetched data
        const characterName = data.name;

        // Display the character name in the DIV#character
        $('div#character').text(characterName);
    });
});
