 #include <queue>

 using namespace std;

class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        curr = root;
        inorder(curr);
    }
    
    int next() {
        int val = s.front();
        s.pop();
        return val;
    }
    
    bool hasNext() {
        return !s.empty();
    }

    void inorder(TreeNode* root) {
        if (root != NULL) {
            inorder(root->left);
            s.push(root->val);
            inorder(root->right);
        }
    }

    TreeNode* curr;
    queue<int> s;
};
