/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let ans = '';
    for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
        const a = word1[i];
        const b = word2[i];
        if (a) ans += a;
        if (b) ans += b;
    }
    return ans;
};