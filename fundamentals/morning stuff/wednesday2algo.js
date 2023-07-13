const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
	const holeInTheGround = [];

	for (let i = 0; i < str.length; i++) {
		if (str[i] === "(") {
			holeInTheGround.push("(");
		} else if (str[i] === ")") {
			if (holeInTheGround.length === 0) {
				return false; // Premature closing parenthesis
			}
			holeInTheGround.pop();
		}
	}

	return holeInTheGround.length === 0; // If the holeInTheGround is empty, all parentheses are balanced
}

console.log(parensValid(str1)); // Output: true
console.log(parensValid(str2)); // Output: false
console.log(parensValid(str3)); // Output: false
console.log(parensValid(str4)); // Output: false

/*****************************************************************************/






/**
 * Determines whether the string's braces, brackets, and parentheses are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str
 * @returns {boolean} Whether the given string's braces are valid.
 */
const two_str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const two_expected1 = true;

const two_str2 = "D(i{a}l[ t]o)n{e";
const two_expected2 = false;

const two_str3 = "A(1)s[O (n]0{t) 0}k";
const two_expected3 = false;

function bracesValid(str) {
	const holeInTheGround = [];

	for (let i = 0; i < str.length; i++) {
		const char = str[i];

		if (char === "(" || char === "{" || char === "[") {
			holeInTheGround.push(char);
		} else if (char === ")" || char === "}" || char === "]") {
			if (holeInTheGround.length === 0) {
				return false; // for the premature closing bracket(s)
			}

			const openingBracket = holeInTheGround.pop();                     //popping with the first boy in the holeInTheGround

			if (
				(char === ")" && openingBracket !== "(") ||
				(char === "}" && openingBracket !== "{") ||
				(char === "]" && openingBracket !== "[")
			) {
				return false; // Mismatched closing bracket
			}
		}
	}

	return holeInTheGround.length === 0; // If the holeInTheGround is empty, all brackets are balanced
}

console.log(bracesValid(two_str1)); // Should Output: true
console.log(bracesValid(two_str2)); // Should Output: false
console.log(bracesValid(two_str3)); // Should Output: false