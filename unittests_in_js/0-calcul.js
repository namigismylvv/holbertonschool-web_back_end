/**
 * Calculates the sum of two rounded numbers
 * @param {number} a - First number to be rounded
 * @param {number} b - Second number to be rounded
 * @returns {number} - Sum of rounded numbers
 */
function calculateNumber(a, b) {
  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
