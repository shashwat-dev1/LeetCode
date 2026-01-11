class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int curr = 0;
        int maxAlt = 0;

        for (int g : gain) {
            curr += g;
            maxAlt = max(maxAlt, curr);
        }
        return maxAlt;
    }
};