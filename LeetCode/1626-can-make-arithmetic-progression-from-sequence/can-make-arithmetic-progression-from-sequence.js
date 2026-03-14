/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    let d;
    const s = arr.sort((a, b) => {return a - b;});
    for (let i = 0; i < arr.length - 1; i++) {
        const a = s[i];
        const b = s[i + 1];
        const t = b - a;
        if (i === 0) d = t;
        if (d !== t) return false;
    }
    return true;
};