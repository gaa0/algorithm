/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function(s) {
    const sl = s.length;
    for (let i = 1; i <= Math.floor(sl / 2) ; i++) {
        if (s.length % i !== 0) continue;
        const sub = s.slice(0, i);
        let cnt = 0;
        for (let j = 0; j < sl; j += i) {
            if (s.slice(j, j + i) === sub) cnt += 1;
        }
        if (cnt === sl / i) return true;
    }
    return false;
};