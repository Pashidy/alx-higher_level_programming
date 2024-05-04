$(document).ready(function() {
    // When the DIV#toggle_header is clicked
    $('div#toggle_header').click(function() {
        // Toggle the class "red" and "green" on the <header> element
        $('header').toggleClass('red green');
    });
});
