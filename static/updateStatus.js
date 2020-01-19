$(document).ready(function(){
    $('.updateButton').on('click', function(){
        $('.loader-wrapper').addClass('is-active');
        setTimeout(function(){
            $('.loader-wrapper').removeClass('is-active');
        }, 3000)
    })

})