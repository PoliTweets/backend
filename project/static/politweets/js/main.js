$(document).ready(function () {
    $("input:radio").change(function () {
        var correct_answer = $('#party_key').val(); // Correct answer is placed in hidden input at this stage.
        var answer = $('input:radio:checked').val(); // Get answer
        $('#party_key').val(answer); // Replace correct answer with current one in hidden form input.

        $('input:radio').attr("disabled",true);
        $('#correct_answer').show();
        $('#nextButton').show();
    });
});
