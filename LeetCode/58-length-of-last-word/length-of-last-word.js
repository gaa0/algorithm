/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let len = 0;
    let i = s.length - 1;

    while (s[i] === ' ') i--;
    while (i >= 0 && s[i] !== ' ') {
        len++;
        i--;
    };

    return len;
};