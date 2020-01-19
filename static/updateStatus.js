$(document).ready(function() {
    $('.updateButton').on('click', function() {
        $('.loader-wrapper').addClass('is-active');
        window.location.replace("/RebuildStatus/" + fid);
    });
});