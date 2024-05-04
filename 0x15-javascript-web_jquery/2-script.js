$(document).ready(function() {
    // When the DIV#red_header is clicked
    $('div#red_header').click(function() {
        // Select the <header> element
        const headerElement = $('header');

        // Update the text color to red (#FF0000)
        headerElement.css('color', '#FF0000');
    });
});
