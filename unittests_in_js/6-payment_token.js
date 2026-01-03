/**
 * Gets a payment token from the API
 * @param {boolean} success - Whether the API call should succeed
 * @returns {Promise|undefined} - A promise that resolves with the API response or undefined
 */
function getPaymentTokenFromAPI(success) {
  if (success) {
    return Promise.resolve({ data: 'Successful response from the API' });
  }
  // If success is false, the function does nothing (returns undefined)
}

module.exports = getPaymentTokenFromAPI;
