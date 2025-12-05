/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const myStack = [];
    for (const item of s) {
        const stackLength = myStack.length
        if (item === '(' || item === '[' || item === '{') {
            myStack.push(item);
        } else {
            if (item === ')') {
                if (myStack[stackLength - 1] === '(') {
                    myStack.pop();
                } else {
                    return false;
                }
            } else if (item === ']') {
                if (myStack[stackLength - 1] === '[') {
                    myStack.pop();
                } else {
                    return false;
                }
            } else if (item === '}') {
                if (myStack[stackLength - 1] === '{') {
                    myStack.pop();
                } else {
                    return false;
                }
            }
        }
    }
    if (myStack.length === 0) {
        return true;
    } else {
        return false;
    }
};