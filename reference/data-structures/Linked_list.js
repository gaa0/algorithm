class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    append(data) {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let current = this.head;
        while (current.next) current = current.next;
        current.next = newNode;
    }

    traverse() {
        let current = this.head;
        while (current) {
            console.log(current.data);
            current = current.next;
        }
    }
}

const myLinkedList = new LinkedList();

myLinkedList.append(1);
myLinkedList.append(2);
myLinkedList.append(3);

myLinkedList.traverse();