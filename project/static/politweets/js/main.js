$(document).ready(function() {
    $("input:button").click(function() {
        var answer_key = this.id; // Get the user's answer (key)
        $("#" + answer_key).css({"background-color": "#E3252A", "color": "white", "border-color": "white"}); // Highlight the user's answer (shown as wrong by default)
        var correct_answer_key = $('#party_key').val(); // Get the correct answer (key) from a hidden field
        $("#" + correct_answer_key).css({"background-color": "#00A5FF", "color": "white", "border-color": "white"}); // Highlight the correct answer (overwrites the above in case of a match)
        //var answer = this.value; // Get the user's answer (full name)
        $('#party_key').val(answer_key); // Replace the correct answer with the one from the user in the hidden field
        $('input:button').attr("disabled", true); // Disable the buttons
        $('#correct_answer').show(); // Show the author of the Tweet
        $('#nextButton').show(); // Show the button to go to the next round
    });
});
