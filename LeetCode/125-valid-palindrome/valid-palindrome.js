/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let letterArray = [];
    for (const letter of s) {
        if ("a" <= letter && letter <= "z") {
            letterArray.push(letter);
        } else if ("A" <= letter && letter <= "Z") {
            letterArray.push(letter.toLowerCase());
        } else if ("0" <= letter && letter <= "9") {
            letterArray.push(letter);
        }
    }
    const lowercase = letterArray.join('');
    const lettersLength = lowercase.length;
    const halfLength = Math.floor(lettersLength / 2);
    for (let i = 0; i < halfLength; i++) {
        if (lowercase[i] !== lowercase[lettersLength - 1 - i]) return false;
    }
    return true;
};