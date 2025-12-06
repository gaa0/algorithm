const myQueue = [];

const myQueueWithElements = [1, 2, 3, 4, 5];

myQueue.push(6);
myQueue.push(7);

const poppedElement = myQueue.shift();

const peekElement = myQueue[0];

const isEmpty = myQueue.length === 0;

for (const element of myQueueWithElements) {
    console.log(element);
}