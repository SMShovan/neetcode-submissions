class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pre;
        vector<int> post;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++){
            pre.push_back(1);
            post.push_back(1); 
        }

        for (int i = 1; i < nums.size(); i++){
            pre[i] = pre[i - 1] * nums[i - 1];
        }
        for (int j = nums.size() - 2; j >= 0; j--){
            post[j] = post[j + 1] * nums[j + 1];
        }
        for (int i = 0; i < nums.size(); i++)
            res.push_back(pre[i] * post[i]);
        return res;
    }
};