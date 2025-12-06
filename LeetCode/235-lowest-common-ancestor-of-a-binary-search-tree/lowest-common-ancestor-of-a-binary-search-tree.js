/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    let foundP = false;
    let foundQ = false;
    const nodeMap = new Map();

    function traverse(parents, node) {
        if ((foundP && foundQ) || node === null) return;
        if (node.val === p.val) {
            foundP = true;
        } else if (node.val === q.val) {
            foundQ = true;
        }

        nodeMap.set(node.val, { treeNode: node, children: new Set() })
        nodeMap.get(node.val).children.add(node.val);
        for (const parent of parents) {
            nodeMap.get(parent).children.add(node.val);
        }

        traverse([...parents, node.val], node.left);
        traverse([...parents, node.val], node.right);
    }

    traverse([root.val], root);

    nodeArray = Array.from(nodeMap.entries());
    for (let i = nodeMap.size - 1; i >= 0; i--) {
        entry = nodeArray[i];
        childrenSet = entry[1].children;
        if (childrenSet.has(p.val) && childrenSet.has(q.val)) {
            return entry[1].treeNode;
        }
    }
};