// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/account/apikeys
const stripe = Stripe('pk_test_TxRiGYlNAKfUBKR7QSpDZG8B00sLDBhhBj');
const elements = stripe.elements();


// Set up Stripe.js and Elements to use in checkout form
const style = {
  base: {
    color: "#32325d",
  }
};

const card = elements.create("card", { style: style });
card.mount("#card-element");


card.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});


const submitButton = document.getElementById('stripeBtn');

submitButton.addEventListener('click', function(ev) {
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
      billing_details: {
        name: 'Jenny Rosen'
      }
    }
  }).then(function(result) {
    if (result.error) {
      // Show error to your customer (e.g., insufficient funds)
      console.log(result.error.message);
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
      }
    }
  });
});

const currentCardForm = $('.current-card-form');
const newCardForm = $('.new-card-form');
const use_default_card = document.querySelector("input[name=use_default_card]");

use_default_card.addEventListener('change', function() {
  if (this.checked) {
    newCardForm.hide();
    currentCardForm.show()
  } else {
    newCardForm.show();
    currentCardForm.hide()
  }
});
