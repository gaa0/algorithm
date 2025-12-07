/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let left = 0;
    let right = 1;

    let turn = 1;
    while (right < nums.length) {
        if (nums[left] === 0 && nums[right] !== 0) {
            let temp;
            temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
        }
        right++;
        if (right === nums.length) {
            left = turn;
            right = left + 1;
            turn++;
        }
    }
};