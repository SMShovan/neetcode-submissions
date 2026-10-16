class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;

        int most = 0;

        while (left < right){
            int candidate = min(heights[left], heights[right]) * (right - left);
            most = max(candidate, most);

            if (heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }
        }
        return most;
    }
};
