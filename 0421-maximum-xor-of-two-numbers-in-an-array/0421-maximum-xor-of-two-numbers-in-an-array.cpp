
class TrieNode {
public:
    TrieNode* child[2];
    TrieNode() {
        child[0] = nullptr;
        child[1] = nullptr;
    }
};

class Solution {
private:
    int ans;
    TrieNode* root;

    std::vector<int> binn(int num) {
        std::vector<int> b;
        while (num > 0) {
            b.push_back(num % 2);
            num /= 2;
        }
        while (b.size() < 32)
            b.push_back(0);
        std::reverse(b.begin(), b.end());
        return b;
    }

    void insert(int num) {
        std::vector<int> binary = binn(num);
        ans = std::max(ans, Xor(binary));

        TrieNode* curr = root;
        for (int dig : binary) {
            if (!curr->child[dig])
                curr->child[dig] = new TrieNode();
            curr = curr->child[dig];
        }
    }

    int Xor(std::vector<int>& binary) {
        int xor_val = 0;
        int p = 31;
        TrieNode* curr = root;

        for (int dig : binary) {
            int other_dig = 1 - dig;
            if (curr->child[other_dig]) {
                curr = curr->child[other_dig];
                xor_val += (1 << p);
            } else {
                if (!curr->child[dig])
                    return xor_val;
                curr = curr->child[dig];
            }
            p--;
        }
        return xor_val;
    }

public:
    int findMaximumXOR(std::vector<int>& nums) {
        ans = 0;
        root = new TrieNode();

        for (int num : nums)
            insert(num);

        return ans;
    }
};
