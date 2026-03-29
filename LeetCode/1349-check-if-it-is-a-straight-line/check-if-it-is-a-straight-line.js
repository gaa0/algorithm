/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    const [x1, y1] = coordinates[0];
    const [x2, y2] = coordinates[1];
    let g = (y2 - y1) / (x2 - x1);
    let b;
    if (g === Infinity) b = y1;
    else b = y1 - g * x1;
    for (let i = 2; i < coordinates.length; i++) {
        const [tx, ty] = coordinates[i];
        if (g === Infinity) {
            if (tx !== x1) return false;
            else continue;
        }
        if (ty !== g * tx + b) return false;
    }
    return true;
};