class Solution {
    public int longestValidParentheses(String s) {
        int maxLen = 0;
        
        // Left to right pass
        int left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            
            if (left == right) {
                // Valid substring found
                maxLen = Math.max(maxLen, 2 * right);
            } else if (right > left) {
                // Reset: too many ')'
                left = right = 0;
            }
        }
        
        // Right to left pass
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            
            if (left == right) {
                // Valid substring found
                maxLen = Math.max(maxLen, 2 * left);
            } else if (left > right) {
                // Reset: too many '('
                left = right = 0;
            }
        }
        
        return maxLen;
    }
}