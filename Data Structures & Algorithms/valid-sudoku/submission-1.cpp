class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        unordered_set<string> seen;

        int row = board.size();
        int col = board[0].size();

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                
                if (board[r][c] == '.') {
                    continue;
                }

                string patternR = "r" + to_string(r) + board[r][c];
                string patternC = "c" + to_string(c) + board[r][c];
                string patternB = "B" + to_string(r / 3) + to_string(c / 3) + board[r][c];

                if (seen.find(patternR) != seen.end() ||
                    seen.find(patternC) != seen.end() ||
                    seen.find(patternB) != seen.end()) {
                    return false;
                }

                seen.insert(patternR);
                seen.insert(patternC);
                seen.insert(patternB);
            }
        }

        return true;
    }
};