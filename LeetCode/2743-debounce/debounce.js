/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let flag = 0;
    let s;
    return function(...args) {
        if (flag) {
            clearTimeout(s);
            clearTimeout(s2);
        }
        s = setTimeout(() => fn(...args), t);
        flag = 1;
        s2 = setTimeout(() => {flag = 0;}, t);
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */