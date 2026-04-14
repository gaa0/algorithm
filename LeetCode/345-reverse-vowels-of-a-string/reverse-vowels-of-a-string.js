/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vowels = [];
    for (const str of s) {
        if (['a', 'e', 'i', 'o', 'u'].includes(str.toLowerCase())) vowels.push(str);
    }
    let ans = '';
    let i = vowels.length - 1;
    for (const str of s) {
        if (['a', 'e', 'i', 'o', 'u'].includes(str.toLowerCase())) {
            ans += vowels[i];
            i--;
        } else {
            ans += str
        }
    }
    return ans;
};