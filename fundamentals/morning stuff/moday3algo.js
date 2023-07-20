// Overall time complexity:
//O(n * n) = O(n^2).
function findBalanceIndex(nums) {
	const len = nums.length;

	for (let i = 0; i < len; i++) {
		const leftSum = nums.slice(0, i).reduce((acc, curr) => acc + curr, 0); //num slice(0,i) creates array including nums elements. Extracts the element on the
		const rightSum = nums.slice(i + 1).reduce((acc, curr) => acc + curr, 0);

		if (leftSum === rightSum) {
			return i;
		}
	}
	return -1;
}

// Test case 1
const two_nums1 = [-2, 5, 7, 0, 3];
const two_expected1 = 2;

// Test case 2
const two_nums2 = [9, 9];
const two_expected2 = -1;

console.log(findBalanceIndex(two_nums1) === two_expected1); // true
console.log(findBalanceIndex(two_nums2) === two_expected2); // true