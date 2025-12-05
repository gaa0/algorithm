/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    if (!list2) return list1;
    if (!list1) return list2;

    const myArray = [];
    let current = list1;
    while (current) {
        myArray.push(current.val);
        current = current.next;
    }
    current = list2;
    while (current) {
        myArray.push(current.val);
        current = current.next;
    }
    sortedArray = myArray.sort((x, y) => x - y);

    function push(answer, val) {
        const myNode = new ListNode(val);
        let current = answer;
        while (current.next) current = current.next;
        current.next = myNode;
        return answer;
    }

    let answer = new ListNode(sortedArray[0]);
    for (let i = 1; i < sortedArray.length; i++) {
        answer = push(answer, sortedArray[i]);
    }

    return answer;
};