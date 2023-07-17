
/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello    world     ";
const expected2 = "hello    world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function myTrim(str) {
    let start = 0;
    let end = string.length;

    //     # Find the index of the first non-whitespace character
    function isWhitespace (char) {
        const whitespaceCharacters = [' ','\t', '\n']; // for spces tabs and newline
        return whitespaceCharacters.includes(char);   //include

    }

    //index of first non-whitespace
    while (start < end && isWhitespace(string[start])) {
        start++;
    }

    //index of last non-whitespace
}


// def myTrim(string):
//     start = 0
//     end = len(string)
    
//     # Find the index of the first non-whitespace character
//     while start < end and string[start].isspace():
//         start += 1
    
//     # Find the index of the last non-whitespace character
//     while end > start and string[end - 1].isspace():
//         end -= 1
    
//     # Return the trimmed string
//     return string[start:end]


/*****************************************************************************/

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.

  Is there a quick way to determine if they aren't an anagram before spending more time?

  Given two strings
  return whether or not they are anagrams
*/

const two_strA1 = "yes";
const two_strB1 = "eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {}



    return string[start:end]