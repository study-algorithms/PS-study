
class Solution {
public:
    bool search(TreeNode* root, int rootVal) {
        if (root == nullptr) return true;

        bool a = search(root->left, rootVal);
        if (root->right->val < root->val || root->left->val > root->val 
        || root->right->val < rootVal || root->left->val < rootVal) {
            return false;
        }
        bool b = search(root->right, rootVal);

        return a && b;
    }

    bool isValidBST(TreeNode* root) {
        int rootVal = root->val;

        return search(root, rootVal);

        // bool con3 = isValidBst(root->left);
        // if (root->right->val < root->val || root->left->val > root->val
        // || root->right->val > rootVal || root->left->val > rootVal) {
        //     return false;
        // }
        // bool con4 = isValidBst(root->right);
    }
};

class Solution {
public:
vector<int> numbers;

    void inorder(TreeNode* root) {
        if (root == nullptr) return;

        inorder(root->left);
        numbers.push_back(root->val);
        inorder(root->right);
    }

    bool isValidBST(TreeNode* root) {
        inorder(root);

        for (int i = 1; i < numbers.size(); i++) {
            if (numbers[i] <= numbers[i-1]) return false;
        }
        return true;
    }
};

/*
Problem
1. Binary Search Tree Validation
2. Left node smaller than root
3. Right node greater than root
4. Children subtree is null if !exists

Workflow:
1. At each traversal, check left node and right node
2. int a = 5;
3. 
*/
