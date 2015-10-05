$(document).ready(function () {
    $("input:radio").change(function () {
        var answer = $('input:radio:checked').val();
        var correct_answer = $('#party_name_key').val();
        $('input:radio').attr("disabled",true);
        $('#correct_answer').show();
        $('#nextButton').show();
    });
});
