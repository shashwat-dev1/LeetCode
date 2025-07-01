class Solution {
public:
    int possibleStringCount(string word) {
        int n = word.length();
        int total = 1; // Original word as is
        int i = 0;

        while (i < n) {
            int j = i;
            // Find the length of the group of same characters
            while (j < n && word[j] == word[i]) {
                ++j;
            }
            int len = j - i;
            if (len >= 2) {
                total += (len - 1); // We can shorten this group in (len-1) ways
            }
            i = j; // Move to the next group
        }

        return total;
    }
};
