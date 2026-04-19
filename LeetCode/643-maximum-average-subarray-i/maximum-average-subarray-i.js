/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
    let i = 0;
    let ans = -1000000;
    let tmp = 0;
    const nl = nums.length;
    while (i < nl) {
        tmp += nums[i];
        if (i >= k - 1) {
            ans = Math.max(ans, tmp);
            tmp -= nums[i - k + 1];
        }
        i++;
    }
    return ans / k;
};