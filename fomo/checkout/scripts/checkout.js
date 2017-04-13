$(function() {

    var handler = StripeCheckout.configure({
  key: 'pk_test_mU3NqMQuhInKGr7gv33Cma25',
  image: 'https://stripe.com/img/documentation/checkout/marketplace.png',
  locale: 'auto',
  token: function(token) {
    // You can access the token ID with `token.id`.
    // Get the token ID to your server-side code for use.
    $('#id_stripe_token').val(token.id);
    $('form').submit()
  }
});

    var cart_total = Math.round($('#cart_total').attr('temp') * 100)

    console.log(cart_total)

   $('form').submit(function(e) {
    //Check if token has been placed
    if($('#id_stripe_token').val() != '') {
        return;
    }
  // Open Checkout with further options:
  handler.open({
    name: 'FOMO Music',
    description: 'Order Payment',
    amount: cart_total
  });
  e.preventDefault();
});

// Close Checkout on page navigation:
window.addEventListener('popstate', function() {
  handler.close();
});


});//ready function
