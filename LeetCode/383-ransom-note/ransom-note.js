/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const ransomMap = new Map();
    const magazineMap = new Map();

    for (const r of ransomNote) {
        if (ransomMap.has(r)) {
            ransomMap.set(r, ransomMap.get(r) + 1);
        } else ransomMap.set(r, 1);
    }

    for (const r of magazine) {
        if (magazineMap.has(r)) {
            magazineMap.set(r, magazineMap.get(r) + 1);
        } else magazineMap.set(r, 1);
    }

    for (const [r, count] of ransomMap.entries()) {
        if (!magazineMap.has(r) || magazineMap.get(r) < count) {
            return false;
        }
    }
    return true;
};