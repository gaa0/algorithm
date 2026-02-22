/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    const pa = [];
    for (let i = 0; i < functions.length; i++) {
        pa.push(functions[i]());
    }
    return Promise.all(pa).then((values) => {return values;});
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */