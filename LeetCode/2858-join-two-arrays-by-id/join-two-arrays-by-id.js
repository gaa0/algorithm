/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const j = [];
    for (const a of arr1.concat(arr2)) {
        j[a['id']] = Object.assign({}, j[a['id']], a);
    }
    return j.filter(e => e !== null);
};