/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let positiveSum = 0;
    let flag = 1;
    for (const num of nums) {
        if (num > 0) {
            positiveSum += num;
        } else {
            flag = 0;
        }
    }
    if (flag == 1) return positiveSum;

    let maxSum = nums[0];

    for (let i = 0; i < nums.length; i++) {
        let currentSum = nums[i];
        maxSum = Math.max(currentSum, maxSum);
        for (let j = i + 1; j < nums.length; j++) {
            currentSum += nums[j];
            maxSum = Math.max(currentSum, maxSum);
            if (currentSum < 0) break;
        }
    }

    return maxSum;
};