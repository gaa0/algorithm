var TimeLimitedCache = function () {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    const existed = this.cache.has(key);
    this.cache.set(key, [value, Date.now() + duration]);
    return existed;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    if (!this.cache.has(key)) return -1;
    const [v, t] = this.cache.get(key);
    if (t < Date.now()) {
        this.cache.delete(key);
        return -1;
    }
    return v;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    for (const [key, [v, t]] of this.cache) {
        if (t < Date.now()) this.cache.delete(key);
    }
    return this.cache.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */