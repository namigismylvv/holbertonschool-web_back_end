const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  describe("SUM operation", function () {
    it("should add two rounded integers", function () {
      assert.strictEqual(calculateNumber("SUM", 1, 3), 4);
    });

    it("should round and add when first number has decimal", function () {
      assert.strictEqual(calculateNumber("SUM", 1.4, 3), 4);
    });

    it("should round and add when second number has decimal", function () {
      assert.strictEqual(calculateNumber("SUM", 1, 3.7), 5);
    });

    it("should round and add when both numbers have decimals", function () {
      assert.strictEqual(calculateNumber("SUM", 1.4, 3.7), 5);
    });

    it("should round up and add when both numbers are at rounding threshold", function () {
      assert.strictEqual(calculateNumber("SUM", 1.5, 3.5), 6);
    });
  });

  describe("SUBTRACT operation", function () {
    it("should subtract two rounded integers", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 5, 3), 2);
    });

    it("should round and subtract when first number has decimal", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 5.4, 3), 2);
    });

    it("should round and subtract when second number has decimal", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 5, 3.7), 1);
    });

    it("should round and subtract when both numbers have decimals", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });

    it("should handle negative results", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 2, 4.5), -3);
    });
  });

  describe("DIVIDE operation", function () {
    it("should divide two rounded integers", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 8, 2), 4);
    });

    it("should round and divide when first number has decimal", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 7.5, 2), 4);
    });

    it("should round and divide when second number has decimal", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 8, 2.5), 2.6666666666666665);
    });

    it("should round and divide when both numbers have decimals", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });

    it('should return "Error" when dividing by zero (rounded)', function () {
      assert.strictEqual(calculateNumber("DIVIDE", 8, 0), "Error");
    });

    it('should return "Error" when dividing by a number that rounds to zero', function () {
      assert.strictEqual(calculateNumber("DIVIDE", 8, 0.4), "Error");
    });
  });
});
