/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    if (nums.length === 1) return nums[0];

    const numsMap = new Map();

    for (const num of nums) {
        if (numsMap.has(num)) {
            cur = numsMap.get(num);
            if (cur + 1 > nums.length / 2) return num;
            numsMap.set(num, cur + 1);
        } else numsMap.set(num, 1);
    }
};