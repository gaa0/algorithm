/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    let sign = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        const a = nums[i];
        const b = nums[i + 1];
        const t = b - a;
        if ((t > 0 && sign < 0) || (t < 0 && sign > 0)) return false;
        if (sign === 0) sign = Math.sign(t);
    }
    return true;
};