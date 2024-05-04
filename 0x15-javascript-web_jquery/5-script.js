$(document).ready(function() {
    // When the DIV#add_item is clicked
    $('div#add_item').click(function() {
        // Create a new <li> element
        var newItem = $('<li>Item</li>');

        // Add the new <li> element to UL.my_list
        $('ul.my_list').append(newItem);
    });
});
