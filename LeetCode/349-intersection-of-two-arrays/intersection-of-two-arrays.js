/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const numsSet1 = new Set();
    const numsSet2 = new Set();

    for (const num of nums1) {
        numsSet1.add(num);
    }

    for (const num of nums2) {
        numsSet2.add(num);
    }

    const answer = [];
    for (const num of numsSet1) {
        if (numsSet2.has(num)) answer.push(num);
    }

    return answer;
};