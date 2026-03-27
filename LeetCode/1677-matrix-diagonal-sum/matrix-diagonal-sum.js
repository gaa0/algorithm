/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let i = 0, j = mat.length - 1;
    let ans = 0;
    while (j >= 0 && i < mat.length) {
        const t = mat[i];
        if (i !== j) ans += t[j];
        ans += t[i];
        i++;
        j--;
    }
    return ans;
};