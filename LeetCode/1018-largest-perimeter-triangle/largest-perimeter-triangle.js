/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    const sortedNums = nums.sort((a, b) => b - a);
    for (let i = 0; i < sortedNums.length - 2; i++) {
        for (let j = i + 1; j < sortedNums.length - 1; j++) {
            for (let k = j + 1; k < sortedNums.length; k++) {
                const [s1, s2, s3] = [sortedNums[i], sortedNums[j], sortedNums[k]];
                console.log(s1, s2, s3);
                if (s1 - s2 - s3 < 0) return s1 + s2 + s3;
                else break;
            }
        }
    }
    return 0;
};