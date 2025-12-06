/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let current = nums[0];
    let max = nums[0];

    for (let i = 1; i < nums.length; i++) {
        current = Math.max(nums[i], current + nums[i]);
        max = Math.max(max, current);
    }

    return max;
};