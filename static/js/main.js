$(document).ready(function() {
    // Initially hide the reserve price field
    $('#reserve_price').hide();

    // Add a change event listener to the reserve status radio buttons
    $('input[name="reserve_status"]').change(function() {
        // if value == reserve
        if (this.value === 'b15a08c1-5603-476c-8171-91437fc7d4ae') {
            $('#reserve_price').show();
        } else {
            $('#reserve_price').hide();
        }
    });
});
