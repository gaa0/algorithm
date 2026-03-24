/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    let ans = Math.floor((high - low) / 2);
    if (low % 2 === 1 || high % 2 === 1) ans++;
    return ans;
};