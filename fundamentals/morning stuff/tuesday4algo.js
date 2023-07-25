const two_num1 = 0;
const two_expected1 = 0;

const two_num2 = 1;
const two_expected2 = 1;

const two_num3 = 2;
const two_expected3 = 1;

const two_num4 = 3;
const two_expected4 = 2;

const two_num5 = 4;
const two_expected5 = 3;

const two_num6 = 8;
const two_expected6 = 21;


function recursiveFib(input){
    input = Math.floor(input);
    if(input <= 1) return input;
    else return recursiveFib(input-1) + recursiveFib(input-2);
}


console.log(recursiveFib(two_num1));
console.log(recursiveFib(two_num2));
console.log(recursiveFib(two_num3));
console.log(recursiveFib(two_num4));
console.log(recursiveFib(two_num5));
console.log(recursiveFib(two_num6));









const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

/**
 * Recursively multiples 1 to the given int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} n The int to factorial. Treat negatives as zero and
 *    floor decimals.
 * @returns {number} The result of !n.
 */
function factorial(input) {
    input = Math.floor(input);
    if (input ==0) return 1;
    return input * factorial(input - 1);
}

console.log(factorial(num1));
console.log(factorial(num2));
console.log(factorial(num3));