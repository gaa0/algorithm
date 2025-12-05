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
                if (myStack[stackLength - 1] !== '(') return false;
                myStack.pop();
            } else if (item === ']') {
                if (myStack[stackLength - 1] !== '[') return false;
                myStack.pop();
            } else if (item === '}') {
                if (myStack[stackLength - 1] !== '{') return false;
                myStack.pop();
            }
        }
    }
    return myStack.length === 0;
};