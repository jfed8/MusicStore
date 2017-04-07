$(function() {
    var images = $('.product_picture');
    images.hide();
    var current = 0;

    $(images[0]).show();

    console.log(images.length)
    $('#btn_next').click(function() {
        $(images[current]).hide();
        current++;
        if (current >= images.length) {
            current = 0;
        }//if
        $(images[current]).show();
    });//click

    $('#btn_previous').click(function() {
        $(images[current]).hide();
        current--;
        if (current < 0) {
            current = images.length - 1;
        }//if
        $(images[current]).show();
    });//click

});//ready
