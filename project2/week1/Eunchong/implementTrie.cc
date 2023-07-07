class Trie {
public:
    struct Node {
        Node* tn[26];
        bool wordEnd;

        Node(): wordEnd(false) {
            for (int i = 0; i < 26; i++) {
                tn[i] = NULL;
            }
        }
    };

    Trie() {
        root = new Node();
    }
    
    void insert(string word) {
        Node* cur = root;

        for (int i = 0; i < word.size(); i++) {
            int idx = word[i] - 'a';
            if (cur->tn[idx] == NULL) cur->tn[idx] = new Node();
            cur = cur->tn[idx];
        }
        cur->wordEnd = true;
    }
    
    bool search(string word, bool prefix = false) {
        Node* cur = root;

        for (int i = 0; i < word.size(); i++) {
            int idx = word[i] - 'a';
            if (cur->tn[idx] == NULL) return false;
            cur = cur->tn[idx];
        }
        if (prefix = false) return cur->wordEnd;
        return true;
    }
    
    bool startsWith(string prefix) {
        return search(prefix, true);
    }

private:
    Node* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
