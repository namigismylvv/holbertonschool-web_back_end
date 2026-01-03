const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function() {
  let consoleLogSpy;

  // Set up the spy before each test
  beforeEach(function() {
    // Create a spy on console.log
    consoleLogSpy = sinon.spy(console, 'log');
  });

  // Clean up after each test
  afterEach(function() {
    // Restore the spy to prevent test pollution
    consoleLogSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', function() {
    // Call the function with 100 and 20
    sendPaymentRequestToApi(100, 20);
    
    // Verify console.log was called with the correct message
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWithExactly('The total is: 120')).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', function() {
    // Call the function with 10 and 10
    sendPaymentRequestToApi(10, 10);
    
    // Verify console.log was called with the correct message
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWithExactly('The total is: 20')).to.be.true;
  });
});
