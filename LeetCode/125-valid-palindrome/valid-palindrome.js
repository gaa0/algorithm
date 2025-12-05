/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let lowercase = "";
    for (const letter of s) {
        if ("a" <= letter && letter <= "z") {
            lowercase += letter;
        } else if ("A" <= letter && letter <= "Z") {
            lowercase += letter.toLowerCase();
        } else if ("0" <= letter && letter <= "9") {
            lowercase += letter;
        }
    }

    const lettersLength = lowercase.length;
    const halfLength = lettersLength / 2;
    for (let i = 0; i < halfLength; i++) {
        if (lowercase[i] !== lowercase[lettersLength - 1 - i]) return false;
    }
    return true;
};