class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1)
            return new TreeNode(val, root, NULL);

        queue<TreeNode*> q;
        q.push(root);

        while(depth--) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                if (depth > 1) {
                    if (q.front()->left) q.push(q.front()->left);
                    if (q.front()->right) q.push(q.front()->right);
                } else {
                    q.front()->left = new TreeNode(val, q.front()->left, NULL);
                    q.front()->right = new TreeNode(val, NULL, q.front()->right);
                }
                q.pop();
            }
        }
        return root;
    }
};
