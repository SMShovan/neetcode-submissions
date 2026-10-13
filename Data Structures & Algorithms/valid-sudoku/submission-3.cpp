class Solution{
public:
    bool isValidSudoku(vector<vector<char>>& board){
        unordered_set<string> seen;

        for (int i = 0; i < board.size(); i++){
            for (int j = 0; j < board[0].size(); j++){
                if (board[i][j] == '.'){
                    continue;
                }

                string row = "r" + std::to_string(i) + std::to_string(board[i][j]);
                string col = "c" + std::to_string(j) + std::to_string(board[i][j]);
                string box = "b" + std::to_string(i / 3) + std::to_string(j / 3) + std::to_string(board[i][j]);

                if (seen.find(row) != seen.end() or seen.find(col) != seen.end() or seen.find(box) != seen.end())
                    return false;

                seen.insert(row);
                seen.insert(col);
                seen.insert(box);

            }
        }
        return true;
    }
};


// class Solution {
// public:
//     bool isValidSudoku(vector<vector<char>>& board) {
        
//         unordered_set<string> seen;

//         int row = board.size();
//         int col = board[0].size();

//         for (int r = 0; r < row; r++) {
//             for (int c = 0; c < col; c++) {
                
//                 if (board[r][c] == '.') {
//                     continue;
//                 }

//                 string patternR = "r" + to_string(r) + board[r][c];
//                 string patternC = "c" + to_string(c) + board[r][c];
//                 string patternB = "B" + to_string(r / 3) + to_string(c / 3) + board[r][c];

//                 if (seen.find(patternR) != seen.end() ||
//                     seen.find(patternC) != seen.end() ||
//                     seen.find(patternB) != seen.end()) {
//                     return false;
//                 }

//                 seen.insert(patternR);
//                 seen.insert(patternC);
//                 seen.insert(patternB);
//             }
//         }

//         return true;
//     }
// };