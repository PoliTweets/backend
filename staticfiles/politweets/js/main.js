 $(document).ready(function () {
    $("input:radio").change(function () {
        console.log($('input:radio[name=type]:checked').val());
        console.log($('#party_name_key').val());
        if ($('input:radio[name=type]:checked').val() == $('#party_name_key').val()) {
            alert('OK');
            //$('#select-table > .roomNumber').attr('enabled',false);
        } else {
            alert('NO OK');
        }
    });
});
