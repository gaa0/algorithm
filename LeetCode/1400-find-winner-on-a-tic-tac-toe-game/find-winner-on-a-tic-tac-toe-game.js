/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function (moves) {
    const grid = [['', '', ''], ['', '', ''], ['', '', '']];
    for (let i = 0; i < moves.length; i++) {
        const [r, c] = moves[i];
        const player = i % 2 === 0 ? 'A' : 'B';
        grid[r][c] = player;
        if (i < 4) continue;

        if (grid[r][0] === player && grid[r][1] === player && grid[r][2] === player) return player;
        if (grid[0][c] === player && grid[1][c] === player && grid[2][c] === player) return player;
        if (r === c && grid[0][0] === player && grid[1][1] === player && grid[2][2] === player) return player;
        if (r + c === 2 && grid[2][0] === player && grid[1][1] === player && grid[0][2] === player) return player;
    }
    return moves.length === 9 ? 'Draw' : 'Pending';
};