/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const sMap = new Map();

    for (const letter of s) {
        if (sMap.has(letter)) {
            sMap.set(letter, sMap.get(letter) + 1);
        } else sMap.set(letter, 1);
    }

    let answer = 0;
    let odd = 0;
    for (const count of sMap.values()) {
        if (count % 2 === 1) {
            odd = 1;
            answer += count - 1;
        } else answer += count;
    }

    return answer + odd;
};