/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function(n) {
        let start = 0;
        let end = n;
        let min = end;
        while (start < end) {
            const m = Math.round((start + end) / 2);
            if (isBadVersion(m)) {
                end = m - 1;
                min = Math.min(min, m);
            } else {
                start = m;
            }
        }
        return min;
    };
};