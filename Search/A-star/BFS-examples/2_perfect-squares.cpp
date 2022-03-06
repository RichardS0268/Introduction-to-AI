// https://leetcode.com/problems/perfect-squares/
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int numSquares(int n) {
        vector<int> f(n + 1, n); // record the shortest path to current node, initialize the vector with the max num -- n
        queue<int> q;
        f[0] = 0;
        q.push(0);
        while (!q.empty()) {
            int s = q.front();
            if (s == n) // break
                break;
            q.pop();
            for (int i = 1; s + i*i <= n; i++){ // add neighbors
                if (f[s + i*i] > f[s] + 1){ // reset the num
                    f[s + i*i] = f[s] + 1;
                    q.push(s + i*i);
                }
            }
            
        }
     	return f[n];       
    }
};