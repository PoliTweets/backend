$(document).ready(function () {
    $("input:radio").change(function () {
        var answer = $('input:radio:checked').val();
        var correct_answer = $('#party_name_key').val();
        alert('You selected '+answer+', the correct answer is '+correct_answer);
    });
});
