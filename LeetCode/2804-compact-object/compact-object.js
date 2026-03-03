/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
    const ofunc = function (o) {
        for (let [k, v] of Object.entries(o)) {
            if (v !== null && typeof v === "object") {
                v = ofunc(v);
                o[k] = v;
            }
            if (!v) {
                if (Array.isArray(o)) {
                    const i = o.indexOf(v);
                    o[i] = null;
                } else {
                    delete o[k];
                }
            }
        }
        if (Array.isArray(o)) o = o.filter(i => i !== null);
        return o;
    }
    return ofunc(obj);
};