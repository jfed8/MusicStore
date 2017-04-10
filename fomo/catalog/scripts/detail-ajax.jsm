$(function() {
    console.log('Hello ajax');
    $("#cart_count").html("${request.user.get_cart_count()}");

    //Ajax Form
    var options = {
        target:     '#purchase_container',     //target element(s) to be update with server response
    };//options

    $('#formlib-purchaseform').ajaxForm(options);//Ajax Form
});//ready
