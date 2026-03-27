/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let i = 0, j = mat.length - 1;
    let ans = 0;
    while (j >= 0) {
        const row = mat[i];
        if (i !== j) ans += row[j];
        ans += row[i];
        i++;
        j--;
    }
    return ans;
};