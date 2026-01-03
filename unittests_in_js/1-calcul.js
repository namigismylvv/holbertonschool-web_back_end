/**
 * Performs arithmetic operations on rounded numbers
 * @param {string} type - Operation type: 'SUM', 'SUBTRACT', or 'DIVIDE'
 * @param {number} a - First number to be rounded
 * @param {number} b - Second number to be rounded
 * @returns {number|string} - Result of the operation or 'Error' for division by zero
 */
function calculateNumber(type, a, b) {
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  switch (type) {
    case "SUM":
      return roundedA + roundedB;
    case "SUBTRACT":
      return roundedA - roundedB;
    case "DIVIDE":
      if (roundedB === 0) {
        return "Error";
      }
      return roundedA / roundedB;
    default:
      throw new Error("Invalid operation type. Use SUM, SUBTRACT, or DIVIDE.");
  }
}

module.exports = calculateNumber;
