/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const ms = [];
    const ns = [];
    const ml = matrix.length;
    const nl = matrix[0].length;
    for (let i = 0; i < ml; i++) {
        for (let j = 0; j < nl; j++) {
            if (matrix[i][j] === 0) {
                ms.push(i);
                ns.push(j);
            }
        }
    }
    for (const m of ms) {
        for (let j = 0; j < nl; j++) matrix[m][j] = 0;
    }
    for (const n of ns) {
        for (let i = 0; i < ml; i++) matrix[i][n] = 0;
    }
};