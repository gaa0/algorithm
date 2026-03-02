/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let ans = [];
    const f = function (p, m) {
        if (n === m) {
            ans.push(p);
        } else {
            if (typeof p === "number") {
                ans.push(p);
            } else {
                for (const pp of p) {
                    f(pp, m + 1);
                }
            }
        }
    }
    for (const a of arr) {
        f(a, 0);
    }
    return ans;
};