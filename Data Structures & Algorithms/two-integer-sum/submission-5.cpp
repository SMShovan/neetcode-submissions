class Solution{
public: 
    vector<int> twoSum (vector<int>& nums, int target){
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++){
            int num = nums[i];
            if (seen.find(target - num) != seen.end() ){
                return {seen[target - num], i};
            }
            seen[num] = i;
        }
        return {};
    }
};

// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
        
//         unordered_map<int, int> seen;

//         for (int i = 0; i < nums.size(); i++) {
//             int num = nums[i];

//             if (seen.find(target - num) != seen.end()) {
//                 return {seen[target - num], i};
//             }

//             seen[num] = i;
//         }

//         return {};
//     }
// };