class Solution{
public:
    vector<int> topKFrequent(vector<int>& nums, int k){
        unordered_map<int, int> mp;

        for (int num : nums){
            mp[num] += 1;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;

        for (auto& item : mp){
            minHeap.push(std::make_pair(item.second, item.first));
            if (minHeap.size() > k){
                minHeap.pop();
            }
        }
        vector<int> res;
        while (!minHeap.empty()){
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res;
    }
};

// class Solution {
// public:
//     vector<int> topKFrequent(vector<int>& nums, int k) {
        
//         unordered_map<int, int> freq;

//         // Count frequency
//         for (int num : nums) {
//             freq[num]++;
//         }

//         // Min heap: {frequency, number}
//         priority_queue<
//             pair<int, int>,
//             vector<pair<int, int>>,
//             greater<pair<int, int>>
//         > minHeap;

//         // Push into heap
//         for (auto& pair : freq) {
//             minHeap.push({pair.second, pair.first});

//             // Keep heap size k
//             if (minHeap.size() > k) {
//                 minHeap.pop();
//             }
//         }

//         // Extract result
//         vector<int> result;

//         while (!minHeap.empty()) {
//             result.push_back(minHeap.top().second);
//             minHeap.pop();
//         }

//         return result;
//     }
// };