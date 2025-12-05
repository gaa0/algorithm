/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;

    const stringS = new Map();

    for (const string of s) {
        if (stringS.has(string)) {
            stringS.set(string, stringS.get(string) + 1);
        } else stringS.set(string, 1);
    }

    for (const string of t) {
        if (stringS.has(string)) {
            stringS.set(string, stringS.get(string) - 1);
        } else return false;
    }
    for (const count of stringS.values()) {
        if (count !== 0) return false;
    }

    return true;
};