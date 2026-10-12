class Solution{
public:
    string encode(vector<string>& strs){

        string res = "";

        for (string s : strs){
            res += to_string(s.size()) + "*" + s;
        }

        return res;

    }

    vector<string> decode(string s){

        vector<string> strs;

        for (int i = 0; i < s.size(); ){
            int j = i; 

            while (s[j] != '*'){
                j++;
            }

            strs.push_back(s.substr(j + 1, stoi(s.substr(i, j - i))));
            i = j + 1 + stoi(s.substr(i, j - i));
        }
        return strs;

    }
};


// class Solution {
// public:

//     string encode(vector<string>& strs) {
        
//         string res = "";

//         for (string s : strs) {
//             res += to_string(s.length()) + "@" + s;
//         }

//         return res;
//     }

//     vector<string> decode(string s) {
        
//         vector<string> strs;
//         int i = 0;

//         while (i < s.length()) {

//             int j = i;

//             // Find delimiter $
//             while (s[j] != '@') {
//                 j++;
//             }

//             // Extract length
//             int length = stoi(s.substr(i, j - i));

//             // Extract actual string
//             string word = s.substr(j + 1, length);

//             strs.push_back(word);

//             // Move to next encoded string
//             i = j + 1 + length;
//         }

//         return strs;
//     }
// };