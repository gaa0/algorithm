/**
 * @param {number[][]} moves
 * @return {string}
 */
var tictactoe = function (moves) {
    const grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
    let i = 0;
    for (const move of moves) {
        let turn;
        if (i % 2 === 0) turn = 'A';
        else turn = 'B';
        i++;
        const x = move[0];
        const y = move[1];
        grid[x][y] = turn;
        if (i < 4) continue;

        let winner = grid[1][1];
        if (winner && ((winner === grid[0][0] && winner === grid[2][2])
            || (winner === grid[2][0] && winner === grid[0][2])
            || (winner === grid[1][0] && winner === grid[1][2])
            || (winner === grid[0][1] && winner === grid[2][1]))) return winner;

        winner = grid[0][0];
        if (winner && (winner === grid[1][0] && winner === grid[2][0])
        || (winner && (winner === grid[0][1] && winner === grid[0][2]))) return winner;

        winner = grid[2][2];
        if (winner && (winner === grid[2][1] && winner === grid[2][0])
        || (winner && (winner === grid[0][2] && winner === grid[1][2]))) return winner;
    }
    if (i < 9) return 'Pending';
    return 'Draw';
};