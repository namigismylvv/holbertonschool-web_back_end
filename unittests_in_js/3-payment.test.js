const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function() {
  it('should use Utils.calculateNumber with correct arguments', function() {
    // Create a spy on the Utils.calculateNumber method
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    
    // Call the function we want to test
    sendPaymentRequestToApi(100, 20);
    
    // Verify the spy was called with the correct arguments
    expect(calculateNumberSpy.calledOnce).to.be.true;
    expect(calculateNumberSpy.calledWithExactly('SUM', 100, 20)).to.be.true;
    
    // Verify the result is correct
    expect(calculateNumberSpy.returnValues[0]).to.equal(120);
    
    // Restore the spy to prevent test pollution
    calculateNumberSpy.restore();
  });
});
