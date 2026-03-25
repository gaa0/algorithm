/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    const s = salary.sort((a, b) => a - b);
    const ss = s.slice(1, s.length - 1);
    const r = ss.reduce((a, b) => a + b, 0);
    return r / ss.length;
};