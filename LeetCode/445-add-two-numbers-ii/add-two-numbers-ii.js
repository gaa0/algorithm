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
    let cl1 = l1;
    let cl2 = l2;
    let s1 = '';
    let s2 = '';
    while (cl1) {
        s1 += cl1.val;
        cl1 = cl1.next;
    }
    while (cl2) {
        s2 += cl2.val;
        cl2 = cl2.next;
    }
    const sum = (BigInt(s1) + BigInt(s2)).toString();
    let dummy = new ListNode(0, null);
    let cur = dummy;
    for (const num of sum) {
        cur.next = new ListNode(Number(num), null);
        cur = cur.next;
    }
    return dummy.next;
};