/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const check = [];
    for (let i = 0; i < nums.length; i++) {
        check.push(false);
    }

    for (const num of nums) {
        if (check[num] === true) return true;
        check[num] = true;
    }

    return false;
};