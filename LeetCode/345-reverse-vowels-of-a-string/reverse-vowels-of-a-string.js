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
    let ans = [];
    let i = vowels.length - 1;
    for (const str of s) {
        if (vs.has(str.toLowerCase())) {
            ans.push(vowels[i]);
            i--;
        } else {
            ans.push(str);
        }
    }
    return ans.join('');
};