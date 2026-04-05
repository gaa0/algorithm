/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const [m, n] = [matrix.length, matrix[0].length];
    const ans = [];
    const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    let [i, d, x, y] = [0, 0, 0, 0];
    while (i < m * n) {
        ans.push(matrix[y][x]);
        matrix[y][x] = 101;
        const [dx, dy] = directions[d];
        const [tx, ty] = [x + dx, y + dy];
        if (tx >= n || ty >= m || tx < 0 || ty < 0 || matrix[ty][tx] === 101) d = (d + 1) % 4;
        [x, y] = [x + directions[d][0], y + directions[d][1]];
        i++;
    }
    return ans;
};