 $(document).ready(function () {
    $("input:radio").change(function () {
        if ($('input:radio[name=type]:checked').val() == $('#party_name_key').value) {
            alert('OK');
        } else {
            alert('NO OK');
        }
    });
});