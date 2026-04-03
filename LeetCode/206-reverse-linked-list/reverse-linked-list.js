/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    const dummy = new ListNode();
    let cur = head;
    while (cur) {
        dummy.next = new ListNode(cur.val, dummy.next);
        cur = cur.next;
    }
    return dummy.next;
};