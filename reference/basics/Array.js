const myArray = [];

const myArrayWithElements = [1, 2, 3, 4, 5];

const multiDimensionalArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

const arrayLength = myArrayWithElements.length;

const element = myArrayWithElements[2];

myArrayWithElements[0] = 10;

myArray.push(6);

myArrayWithElements.splice(2, 1);

for (const item of myArrayWithElements) {
    console.log(item);
}

const index = myArrayWithElements.indexOf(4);

const subArray = myArrayWithElements.slice(1, 4);