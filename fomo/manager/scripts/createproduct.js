$(function () {

    var product_type = $('#id_product_type');

    product_type.change(function() {
        var value = product_type.val();

        if (value == 'BulkProduct') {
            $('#id_barcode').closest('p').show();
            $('#id_quantity').closest('p').show();
            $('#id_reorder_trigger').closest('p').show();
            $('#id_reorder_quantity').closest('p').show();
            $('#id_serial_number').closest('p').hide();
            $('#id_condition').closest('p').hide();
            $('#id_is_rented').closest('p').hide();
            $('#id_due_date').closest('p').hide();
        } else if (value=='UniqueProduct') {
            $('#id_barcode').closest('p').hide();
            $('#id_quantity').closest('p').hide();
            $('#id_reorder_trigger').closest('p').hide();
            $('#id_reorder_quantity').closest('p').hide();
            $('#id_serial_number').closest('p').show();
            $('#id_condition').closest('p').show();
            $('#id_is_rented').closest('p').hide();
            $('#id_due_date').closest('p').hide();
        } else if (value == 'RentalProduct') {
            $('#id_barcode').closest('p').hide();
            $('#id_quantity').closest('p').hide();
            $('#id_reorder_trigger').closest('p').hide();
            $('#id_reorder_quantity').closest('p').hide();
            $('#id_serial_number').closest('p').show();
            $('#id_condition').closest('p').show();
            $('#id_is_rented').closest('p').show();
            $('#id_due_date').closest('p').show();
        }
    });
    product_type.change();

    $('#id_due_date').datetimepicker({
        timepicker: false,
        format: 'Y-m-d'
    });
});
