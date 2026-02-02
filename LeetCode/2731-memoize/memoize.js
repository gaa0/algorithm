/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const m = new Map();
    return function(...args) {
        const s = args.toString();
        if (m.has(s)) {
            return m.get(s);
        } else {
            m.set(s, fn(...args));
            return m.get(s);
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */