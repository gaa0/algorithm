const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

function bfs(x, y, visited, grid) {
    const queue = [[x, y]];
    visited[x][y] = true;

    while (queue.length) {
        const [x, y] = queue.shift();
        console.log(`방문 위치: (${x}, ${y})`);

        for (let d = 0; d < 4; d++) {
            const nx = x + dx[d];
            const ny = y + dy[d];

            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length &&
                !visited[nx][ny] && grid[nx][ny] === 1) {
                    queue.push([nx, ny]);
                    visited[nx][ny] = true;
                }
        }
    }
}

const grid = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1]
]

const visited = [];
for (let i = 0; i < grid.length; i++) {
    const inner = [];
    for (let j = 0; j < grid[0].length; j++) {
        inner.push(false);
    }
    visited.push(inner);
}

bfs(0, 0, visited, grid);