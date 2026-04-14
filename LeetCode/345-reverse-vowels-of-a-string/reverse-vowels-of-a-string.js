/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const vs = new Set(['a', 'e', 'i', 'o', 'u']);
    const vowels = [];
    for (const str of s) {
        if (vs.has(str.toLowerCase())) vowels.push(str);
    }
    let ans = '';
    let i = vowels.length - 1;
    for (const str of s) {
        if (vs.has(str.toLowerCase())) {
            ans += vowels[i];
            i--;
        } else {
            ans += str
        }
    }
    return ans;
};