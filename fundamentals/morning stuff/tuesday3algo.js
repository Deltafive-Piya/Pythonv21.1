function interleaveArrays(arr1, arr2) {
    const combined = [];
    const maxLength = Math.max(arr1.length, arr2.length);
  
    for (let i = 0; i < maxLength; i++) {
      if (i < arr1.length) {
        combined.push(arr1[i]);
      }
  
      if (i < arr2.length) {
        combined.push(arr2[i]);
      }
    }
  
    return combined;
  }
  
  // Test case 1
  const arrA1 = [1, 2, 3];
  const arrB1 = ["a", "b", "c"];
  const expected1 = [1, "a", 2, "b", 3, "c"];
  
  console.log(interleaveArrays(arrA1, arrB1)); // Output: [1, "a", 2, "b", 3, "c"]
  console.log(interleaveArrays(arrB1, arrA1)); // Output: ["a", 1, "b", 2, "c", 3]
  
  // Test case 2
  const arrA2 = [1, 3];
  const arrB2 = [2, 4, 6, 8];
  const expected2 = [1, 2, 3, 4, 6, 8];
  
  console.log(interleaveArrays(arrA2, arrB2)); // Output: [1, 2, 3, 4, 6, 8]
  console.log(interleaveArrays(arrB2, arrA2)); // Output: [2, 1, 4, 3, 6, 8]
  
  // Test case 3
  const arrA3 = [1, 3, 5, 7];
  const arrB3 = [2, 4];
  const expected3 = [1, 2, 3, 4, 5, 7];
  
  console.log(interleaveArrays(arrA3, arrB3)); // Output: [1, 2, 3, 4, 5, 7]
  console.log(interleaveArrays(arrB3, arrA3)); // Output: [2, 1, 4, 3, 5, 7]
  
  // Test case 4
  const arrA4 = [];
  const arrB4 = [42, 0, 6];
  const expected4 = [42, 0, 6];
  
  console.log(interleaveArrays(arrA4, arrB4)); // Output: [42, 0, 6]
  console.log(interleaveArrays(arrB4, arrA4)); // Output: [42, 0, 6]



  /* 
  Array: Binary Search (non recursive)

  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .

  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete

    return how many times the given number occurs
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 8;
const two_expected3 = true;

// bonus, how many times does the search num appear?
const two_nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const two_searchNum4 = 2;
const two_expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
    for (let i = 0; i < sortedNums.length; i++) {
        var index = Math.floor((sortedNums.length - 1) / 2)
        if (searchNum[index] < searchNum) {
            leftArr = sortedNums.slice(0, index);

        }
    }
}