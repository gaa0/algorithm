/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let [n1, n2] = [l1, l2];
    let dummy = new ListNode(0, null);
    let cur = dummy;
    let t = 0;
    while (n1 || n2) {
        let [num1, num2] = [0, 0];
        if (n1) num1 = n1.val;
        if (n2) num2 = n2.val;
        let val = num1 + num2 + t;
        if (val >= 10) {
            t = 1;
            val -= 10;
        } else {
            t = 0;
        }
        cur.next = new ListNode(val, null);
        if (n1) n1 = n1.next;
        if (n2) n2 = n2.next;
        cur = cur.next;
    }
    if (t) cur.next = new ListNode(1, null);
    return dummy.next;
};