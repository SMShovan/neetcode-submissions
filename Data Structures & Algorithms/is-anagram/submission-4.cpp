class Solution {
   public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;

        for (char c : s){
            mp[c]++;
        }

        for (char c : t){
            if (mp.find(c) == mp.end() || mp[c] == 0){
                return false;
            }
            mp[c]--;
        }
        for (auto& pair : mp){
            if (pair.second != 0){
                return false;
            }
        }
        return true;
    }
};

// class Solution {
//    public:
//     bool isAnagram(string s, string t) {
//         unordered_map<char, int> mp;

//         for (char c : s) {
//             mp[c]++;
//         }

//         for (char c : t) {
//             if (mp.find(c) == mp.end() || mp[c] == 0) {
//                 return false;
//             } else {
//                 mp[c]--;
//             }
//         }

//         for (auto& pair : mp) {
//             if (pair.second > 0) {
//                 return false;
//             }
//         }

//         return true;
//     }
// };