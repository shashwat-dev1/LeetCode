/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    pair<int, int> dfs(TreeNode* root) {
        if (!root) return {0, 0};

        auto left = dfs(root->left);
        auto right = dfs(root->right);

        // If we rob this node, we can't rob children
        int rob = root->val + left.first + right.first;

        // If we don't rob this node, we can rob or not rob children
        int skip = max(left.first, left.second) + max(right.first, right.second);

        return {skip, rob};
    }

    int rob(TreeNode* root) {
        auto result = dfs(root);
        return max(result.first, result.second);
    }
};
