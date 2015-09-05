 $(document).ready(function () {
    $("input:radio").change(function () {
        if ($('input:radio[name=type]:checked').val() == $('#party_name_key').value) {
            alert('OK');
            //$('#select-table > .roomNumber').attr('enabled',false);
        } else {
            alert('NO OK');
        }
    });
});
