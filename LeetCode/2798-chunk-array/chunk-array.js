/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const ans = [];
    for (const a of arr) {
        if (ans.length === 0 || [0, size].includes(ans[ans.length - 1].length)) {
            ans.push([a]);
        } else {
            ans[ans.length - 1].push(a);
        }
    }
    return ans;
};
