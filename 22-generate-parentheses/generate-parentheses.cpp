class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;

        function<void(string,int,int)> dfs = [&](string s, int open, int close) {
            if (s.size() == 2 * n) {
                res.push_back(s);
                return;
            }
            if (open < n) dfs(s + "(", open + 1, close);
            if (close < open) dfs(s + ")", open, close + 1);
        };

        dfs("", 0, 0);
        return res;
    }
};