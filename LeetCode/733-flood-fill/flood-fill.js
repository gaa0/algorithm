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
    const st = image[sr][sc];
    if (st === color) return image;

    const myStack = [[sr, sc]];
    while (myStack.length) {
        const [x, y] = myStack.pop();
        image[x][y] = color;

        for (let d = 0; d < 4; d++) {
            const nx = x + dx[d];
            const ny = y + dy[d];
            if (0 <= nx && nx < image.length && 0 <= ny &&
                ny < image[0].length && image[nx][ny] === st) {
                myStack.push([nx, ny]);
            }
        }
    }

    return image;
};