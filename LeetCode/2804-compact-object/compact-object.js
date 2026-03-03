/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (!obj || typeof obj !== "object") return obj;

    if (Array.isArray(obj)) {
        return obj.map(compactObject).filter(Boolean);
    }

    const ans = {};
    for (const k in obj) {
        const v = compactObject(obj[k]);
        if (v) ans[k] = v;
    }
    return ans;
};