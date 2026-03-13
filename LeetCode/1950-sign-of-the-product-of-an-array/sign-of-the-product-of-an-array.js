/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let p = 1;
    for (const num of nums) {
        p *= num;
    }
    if (p > 0) {
        return 1;
    } else if (p < 0) {
        return -1;
    } else {
        return 0;
    }
};