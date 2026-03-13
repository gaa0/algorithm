/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let p = 1;
    for (const num of nums) {
        if (num === 0) return 0;
        if (num < 0) p *= -1;
    }
    return p;
};