$(function() {


    $('#prod_graph').click(function() {
        var productid = $('#prod_graph').attr('temp');

        $.loadmodal({
            url: '/catalog/detail.modal/' + productid,
            title: 'Pictures',
        })
    }); //click

    //Ajax Form
    var options = {
        target:     '#purchase_container',     //target element(s) to be update with server response
    };//options

    $('#formlib-purchaseform').ajaxForm(options);//Ajax Form

});//ready
