const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  describe('SUM operation', function() {
    it('should add two rounded integers', function() {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });

    it('should round and add when first number has decimal', function() {
      expect(calculateNumber('SUM', 1.4, 3)).to.equal(4);
    });

    it('should round and add when second number has decimal', function() {
      expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    });

    it('should round and add when both numbers have decimals', function() {
      expect(calculateNumber('SUM', 1.4, 3.7)).to.equal(5);
    });

    it('should round up and add when both numbers are at rounding threshold', function() {
      expect(calculateNumber('SUM', 1.5, 3.5)).to.equal(6);
    });
  });

  describe('SUBTRACT operation', function() {
    it('should subtract two rounded integers', function() {
      expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    });

    it('should round and subtract when first number has decimal', function() {
      expect(calculateNumber('SUBTRACT', 5.4, 3)).to.equal(2);
    });

    it('should round and subtract when second number has decimal', function() {
      expect(calculateNumber('SUBTRACT', 5, 3.7)).to.equal(1);
    });

    it('should round and subtract when both numbers have decimals', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should handle negative results', function() {
      expect(calculateNumber('SUBTRACT', 2, 4.5)).to.equal(-3);
    });
  });

  describe('DIVIDE operation', function() {
    it('should divide two rounded integers', function() {
      expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
    });

    it('should round and divide when first number has decimal', function() {
      expect(calculateNumber('DIVIDE', 7.5, 2)).to.equal(4);
    });

    it('should round and divide when second number has decimal', function() {
      expect(calculateNumber('DIVIDE', 8, 2.5)).to.equal(2.6666666666666665);
    });

    it('should round and divide when both numbers have decimals', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when dividing by zero (rounded)', function() {
      expect(calculateNumber('DIVIDE', 8, 0)).to.equal('Error');
    });

    it('should return "Error" when dividing by a number that rounds to zero', function() {
      expect(calculateNumber('DIVIDE', 8, 0.4)).to.equal('Error');
    });
  });
});
