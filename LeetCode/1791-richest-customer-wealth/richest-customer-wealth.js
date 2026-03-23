/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let ans = 0;
    for (const account of accounts) {
        ans = Math.max(ans, account.reduce((a, b) => a + b));
    }
    return ans;
};