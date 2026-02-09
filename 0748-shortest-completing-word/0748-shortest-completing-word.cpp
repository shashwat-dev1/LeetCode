class Solution {
public:
    vector<int> countFreq(string s) {
        vector<int> freq(26, 0);
        for (char c : s) {
            if (isalpha(c)) freq[tolower(c) - 'a']++;
        }
        return freq;
    }

    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        vector<int> need = countFreq(licensePlate);
        string ans = "";

        for (string &w : words) {
            vector<int> have = countFreq(w);
            bool ok = true;
            for (int i = 0; i < 26; i++) {
                if (have[i] < need[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok && (ans.empty() || w.size() < ans.size())) {
                ans = w;
            }
        }
        return ans;
    }
};
