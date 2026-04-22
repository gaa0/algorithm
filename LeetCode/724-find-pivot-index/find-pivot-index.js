/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    const sumLeft = [0];
    const sumRight = [0];
    let s = 0;
    const nl = nums.length;
    for (let i = 0; i < nl; i++) {
        s += nums[i];
        sumLeft.push(s);
    }
    s = 0;
    for (let i = nl - 1; i >= 0; i--) {
        s += nums[i];
        sumRight.push(s);
    }
    console.log(sumLeft);
    console.log(sumRight);
    for (let i = 0; i < nl; i++) {
        if (sumLeft[i] === sumRight[nl - i - 1]) return i;
    }
    return -1;
};