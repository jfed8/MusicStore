$(function() {
    //Load DeleteConfirm Modal
    $('.delete_link').click(function(event) {
        // cancel the default behavior
        event.preventDefault();

        $('#DeleteConfirm').modal({
            //no options
        });

        var href = $(this).attr('href');
        $('#finalize_delete').attr('href', href);
    });//click

    //Update product quantity on click
    $('.update_quantity_button').click(function() {
        //Build the url
        var button =$(this);
        var url = '/manager/products.get_quantity/'+ button.attr('data-pid');

        // call ajax
        button.siblings('.quantity_text').load(url);

    })

});//ready
