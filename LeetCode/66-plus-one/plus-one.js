/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let d = '';
    for (const digit of digits) {
        d += String(digit);
    }
    const a = BigInt(d) + BigInt(1);
    const ans = [];
    for (s of String(a)) {
        ans.push(Number(s));
    }
    return ans;
};