$(document).ready(function() {
    $('#btn_translate').click(function() {
        // Get the language code entered by the user
        var languageCode = $('#language_code').val();

        // Fetch translation from the API
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
            // Display the translation of "Hello" in the DIV#hello
            $('#hello').text(data.hello);
        });
    });
});
