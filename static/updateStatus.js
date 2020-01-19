$(document).ready(function() {
    $('.updateButton').on('click', function() {
        $('.loader-wrapper').addClass('is-active');
        $.ajax({
            type : 'GET',
            url : '/RebuildStatus/'.concat(fid),
            success : console.log(fid)
            })
        .done(function(data) {
            $('.loader-wrapper').removeClass('is-active');
            window.location.reload(true); 
        });
    });
});