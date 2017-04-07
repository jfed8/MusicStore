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


});//ready
