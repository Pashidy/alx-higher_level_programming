$(document).ready(function() {
    // Add item to the list
    $('div#add_item').click(function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });

    // Remove item from the list
    $('div#remove_item').click(function() {
        $('ul.my_list li:last-child').remove();
    });

    // Clear the list
    $('div#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});
