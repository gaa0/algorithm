/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const grouped = {};
    for (const item of this) {
        const o = fn(item);
        if (o in grouped) {
            grouped[o].push(item);
        } else {
            grouped[o] = [item];
        }
    }
    return grouped;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */