class TreeNode {
    constructor(value) {
        this.value = value;
        this.children = [];
    }

    addChild(childNode) {
        this.children.push(childNode);
    }    
}

const root = new TreeNode("Root");

const child1 = new TreeNode("Child 1");
const child2 = new TreeNode("Child 2");
const child3 = new TreeNode("Child 3");

root.addChild(child1);
root.addChild(child2);
root.addChild(child3);

const child11 = new TreeNode("Child 1.1");
const child12 = new TreeNode("Child 1.2");

child1.addChild(child11);
child1.addChild(child12);

console.log(root);