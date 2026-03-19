/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function(operations) {
    const records = [];
    for (const operation of operations) {
        if (!isNaN(operation)) {
            records.push(Number(operation));
        } else if (operation === '+') {
            const rl = records.length;
            records.push(records[rl - 2] + records[rl - 1]);
        } else if (operation === 'D') {
            records.push(records[records.length - 1] * 2);
        } else if (operation === 'C') {
            records.pop();
        }
    }
    return records.reduce((a, b) => a + b, 0);
};