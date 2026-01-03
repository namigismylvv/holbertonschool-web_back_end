const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
  it('should return the sum of two rounded integers', function() {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round down a and return the sum', function() {
    assert.strictEqual(calculateNumber(1, 3.3), 4);
  });

  it('should round up a and return the sum', function() {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round down b and return the sum', function() {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
  });

  it('should round up b and return the sum', function() {
    assert.strictEqual(calculateNumber(1.8, 3), 5);
  });

  it('should round both a and b down and return the sum', function() {
    assert.strictEqual(calculateNumber(1.2, 3.2), 4);
  });

  it('should round a down and b up and return the sum', function() {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round a up and b down and return the sum', function() {
    assert.strictEqual(calculateNumber(1.8, 3.2), 5);
  });

  it('should round both a and b up and return the sum', function() {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negative numbers correctly', function() {
    assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
  });

  it('should handle zero values correctly', function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('should handle decimal values at the rounding threshold', function() {
    assert.strictEqual(calculateNumber(1.5, 2.5), 5);
  });
});
