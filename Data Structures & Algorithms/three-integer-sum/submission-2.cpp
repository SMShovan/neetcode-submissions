class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] > 0){
                break;
            }
            else if (i > 0 && nums[i - 1] == nums[i]){
                continue;
            }

            int left = i + 1;
            int right = nums.size() - 1;

            while (left < right){
                int threeSum = nums[i] + nums[left] + nums[right];

                if (threeSum > 0){
                    right--;
                }
                else if (threeSum < 0){
                    left++;
                }
                else{
                    res.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    
                    while (nums[left] == nums[left - 1] && left < right){
                        left++;
                }
                }

                
            }
        }
        return res;
    }
};
