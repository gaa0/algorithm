/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let start = 0;
    let end = nums.length;
    while (start <= end) {
        let idx = 0;
        if ((end + start) % 2 === 0) {
            idx = Math.floor((end + start) / 2);
        } else {
            idx = Math.floor((end + start) / 2);
        }
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