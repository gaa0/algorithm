/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    function dfs(x, y, visited, grid, st, color) {
        const myStack = [[x, y]];
        while (myStack.length) {
            const [x, y] = myStack.pop();
            visited[x][y] = true;
            grid[x][y] = color;

            for (let d = 0; d < 4; d++) {
                const nx = x + dx[d];
                const ny = y + dy[d];
                if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length &&
                    !visited[nx][ny] && grid[nx][ny] === st) {
                    myStack.push([nx, ny]);
                }
            }
        }
        return grid;
    }

    const visited = [];
    for (let i = 0; i < image.length; i++) {
        const inner = [];
        for (let j = 0; j < image[0].length; j++) {
            inner.push(false);
        }
        visited.push(inner);
    }

    return dfs(sr, sc, visited, image, image[sr][sc], color);
};