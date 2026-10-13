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