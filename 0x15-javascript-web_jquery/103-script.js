$(document).ready(function() {
    function fetchTranslation() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Fetch translation from the API
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
            // Display the translation of "Hello" in the DIV#hello
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key
            fetchTranslation();
        }
    });
});
