class Graph {
    constructor() {
        this.nodes = new Set();
        this.edges = new Map();
    }

    addNode(value) {
        this.nodes.add(value);
        this.edges.set(value, []);
    }

    addEdge(fromNode, toNode) {
        if (this.edges.has(fromNode)) this.edges.get(fromNode).push(toNode);
    }

    display() {
        for (const [node, neighbors] of this.edges.entries()) {
            console.log(`${node} -> ${neighbors}`);
        }
    }
}

const myGraph = new Graph();

myGraph.addNode("A");
myGraph.addNode("B");
myGraph.addNode("C");
myGraph.addNode("D");
myGraph.addNode("E");

myGraph.addEdge("A", "B");
myGraph.addEdge("B", "C");
myGraph.addEdge("C", "D");
myGraph.addEdge("D", "E");
myGraph.addEdge("E", "A");

myGraph.display();