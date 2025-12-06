/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
    if (!head) return false;

    let i = 0;
    let node = head;
    while (i < 10000) {
        if (!node.next) return false;
        node = node.next;
        i++;
    }

    return true;
};