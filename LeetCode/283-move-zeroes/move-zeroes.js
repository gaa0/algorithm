/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let insert = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[insert] = nums[i];
            insert++;
        }
    }

    while (insert < nums.length) {
        nums[insert] = 0;
        insert++;
    }
};