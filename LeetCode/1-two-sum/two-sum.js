/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const myMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const comp = target - num;

        if (myMap.has(comp)) {
            return [myMap.get(comp), i];
        };
        
        myMap.set(num, i);
    }
};