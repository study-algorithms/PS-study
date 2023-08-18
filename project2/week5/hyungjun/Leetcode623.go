/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {

	if depth == 1 {
		newNode := &TreeNode{Val: val, Left: root}
		return newNode
	}

	copiedRoot := root
	treeNodePtrs := []*TreeNode{}

	treeNodePtrs = append(treeNodePtrs, getTreeNodes(root, 1, depth)...)
	for _, nodePtr := range treeNodePtrs {
		if nodePtr != nil {
			newNode1 := &TreeNode{Val: val, Left: nodePtr.Left}
			newNode2 := &TreeNode{Val: val, Right: nodePtr.Right}
			nodePtr.Left = newNode1
			nodePtr.Right = newNode2
		}
	}
	return copiedRoot
}

func getTreeNodes(root *TreeNode, cur int, depth int) []*TreeNode {
	if cur == depth-1 {
		return []*TreeNode{root}
	}
	if root == nil {
		return nil
	}
	treeNodes := []*TreeNode{}
	treeNodes = append(treeNodes, getTreeNodes(root.Left, cur+1, depth)...)
	treeNodes = append(treeNodes, getTreeNodes(root.Right, cur+1, depth)...)
	return treeNodes
}