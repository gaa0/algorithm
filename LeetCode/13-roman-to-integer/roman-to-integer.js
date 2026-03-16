/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let ans = 0;
    const sl = s.length;
    const d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for (let i = 0; i < sl; i++) {
        let n = 0;
        const symbol = s[i];
        if (symbol === 'I') {
            if (i < sl - 1 && ['V', 'X'].includes(s[i + 1])) {
                n = -1;
            }
        } else if (symbol === 'X') {
            if (i < sl - 1 && ['L', 'C'].includes(s[i + 1])) {
                n = -10;
            }
        } else if (symbol === 'C') {
            if (i < sl - 1 && ['D', 'M'].includes(s[i + 1])) {
                n = -100;
            }
        }
        if (n === 0) n = d[s[i]];
        ans += n;
    }
    return ans;
};