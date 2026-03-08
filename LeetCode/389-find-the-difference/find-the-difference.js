/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    const so = new Map;
    for (const ss of s) {
        if (so.has(ss)) {
            so.set(ss, so.get(ss) + 1);
        } else {
            so.set(ss, 1);
        }
    }
    for (const tt of t) {
        if (so.has(tt)) {
            const ttt = so.get(tt);
            if (ttt === 0) {
                return tt;
            } else {
                so.set(tt, ttt - 1);
            }
        } else {
            return tt;
        }
    }
};