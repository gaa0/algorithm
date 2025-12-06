/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function (intervals, newInterval) {
    const front = [];
    let middle = newInterval;
    const rear = [];

    function isOverlap(a, b) {
        return (a[0] < b[1] && b[0] <= a[1]) || (b[0] < a[1] && a[0] <= b[1])
    }

    function mergeIntervals(a, b) {
        return [Math.min(a[0], b[0]), Math.max(a[1], b[1])];
    }

    for (let i = 0; i < intervals.length; i++) {
        const a = intervals[i];
        if (isOverlap(a, middle)) {
            middle = mergeIntervals(a, middle);
        } else if (a[1] < middle[0]) {
            front.push(a);
        } else {
            rear.push(a);
        }
    }

    return [...front, middle, ...rear];
};