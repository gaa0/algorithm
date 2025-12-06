const myDeque = [];

const myDequeWithElements = [1, 2, 3, 4, 5];

const dequeLength = myDequeWithElements.length;

myDeque.unshift(0);

myDeque.push(6);

const frontElement = myDeque.shift();

const rearElement = myDeque.pop();

for (const element of myDequeWithElements) {
    console.log(element);
}

const index = myDequeWithElements.indexOf(3);