/**
 * @param {string} instructions
 * @return {boolean}
 */
var isRobotBounded = function(instructions) {
    let [x, y, dx, dy] = [0, 0, 0, 1];
    const directions = [[0, 1], [-1, 0], [0, -1], [1, 0]];
    let d = 0;
    for (const instruction of instructions) {
        if (instruction === "G") {
            [x, y] = [x + dx, y + dy];
        }
        else if (instruction === "L") {
            d = (d + 1) % 4;
        } else {
            d = (d + 3) % 4;
        }
        [dx, dy] = directions[d];
    }
    if (!d && !(!x && !y)) return false;
    return true;
};