/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let start = 0;
    let end = nums.length - 1;
    while (start <= end) {
        let idx = Math.floor((start + end) / 2);
        const st = nums[idx];
        if (target === st) {
            return idx;
        } else if (target < st) {
            end = idx - 1;
        } else {
            start = idx + 1;
        }
    }
    return -1;
};