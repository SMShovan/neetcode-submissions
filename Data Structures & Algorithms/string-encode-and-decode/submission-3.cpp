class Solution {
public:

    string encode(vector<string>& strs) {
        
        string res = "";

        for (string s : strs) {
            res += to_string(s.length()) + "@" + s;
        }

        return res;
    }

    vector<string> decode(string s) {
        
        vector<string> strs;
        int i = 0;

        while (i < s.length()) {

            int j = i;

            // Find delimiter $
            while (s[j] != '@') {
                j++;
            }

            // Extract length
            int length = stoi(s.substr(i, j - i));

            // Extract actual string
            string word = s.substr(j + 1, length);

            strs.push_back(word);

            // Move to next encoded string
            i = j + 1 + length;
        }

        return strs;
    }
};