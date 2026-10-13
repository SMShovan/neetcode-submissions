class Solution{
public:
    int longestConsecutive(vector<int>& nums){
        unordered_set<int> seen;

        for (int num : nums){
            seen.insert(num);
        }

        int res = 0;

        for (int num : nums){
            if (seen.find(num - 1) != seen.end() ){
                continue;
            } 

            int streak = 1;

            while (seen.find(num + streak) != seen.end()){
                streak += 1;
            }

            res = max(res, streak);
        }
        return res;
    }
};

// class Solution {
// public:
//     int longestConsecutive(vector<int>& nums) {
        
//         unordered_set<int> check(nums.begin(), nums.end());

//         int longest = 0;

//         for (int num : nums) {

//             // Start of a sequence
//             if (check.find(num - 1) == check.end()) {

//                 int streak = 1;
//                 int next = num + 1;

//                 while (check.find(next) != check.end()) {
//                     streak++;
//                     next++;
//                 }

//                 longest = max(longest, streak);
//             }
//         }

//         return longest;
//     }
// };