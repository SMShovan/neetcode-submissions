class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        while (left < right){
            while (!std::isalnum(s[left]) and left < right){
                left++;
            }

            while (!std::isalnum(s[right]) and left < right){
                right--;
            }
            if (left < right and std::tolower(s[left]) != std::tolower(s[right])){
                return false;
            }
            left++;
            right--;
        }
        return true;


    }
};
