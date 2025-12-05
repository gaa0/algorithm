const myStack = [];

const myStackWithElements = [1, 2, 3, 4, 5];

myStack.push(6);
myStack.push(7);

const poppedElement = myStack.pop();

const peekElement = myStack[myStack.length - 1];

const isEmpty = myStack.length === 0;

for (const item of myStackWithElements) {
    console.log(item);
}