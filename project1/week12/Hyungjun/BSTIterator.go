/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type BSTIterator struct {
	nodes []*TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
	bstIterator := BSTIterator{nodes: []*TreeNode{}}
	bstIterator.nodes = fillNodes(bstIterator.nodes, root)
	return bstIterator
}

func fillNodes(nodes []*TreeNode, node *TreeNode) []*TreeNode {
	for node != nil {
		nodes = append(nodes, node)
		node = node.Left
	}
	return nodes
}

func (this *BSTIterator) Next() int {
	result := this.nodes[len(this.nodes)-1]
	this.nodes = this.nodes[:len(this.nodes)-1]
	this.nodes = fillNodes(this.nodes, result.Right)
	return result.Val
}

func (this *BSTIterator) HasNext() bool {
	if len(this.nodes) == 0 {
		return false
	}
	return true
}


/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
