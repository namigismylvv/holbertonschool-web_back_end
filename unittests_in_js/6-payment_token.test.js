const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should resolve with the correct response when success is true', function(done) {
    // Call the function with success = true
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Verify the response is correct
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        // Call done to indicate the test is complete
        done();
      })
      .catch((error) => {
        // If there's an error, pass it to done to fail the test
        done(error);
      });
  });
});
