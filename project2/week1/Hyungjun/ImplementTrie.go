type Trie struct {
	children map[rune]*Trie
	isLast bool
}

func Constructor() Trie {
	return Trie{
		children: make(map[rune]*Trie),
		isLast: false,
	}
}

func (this *Trie) Insert(word string) {
	trie := this
	for _, letter := range word {
		if trie.children[letter] == nil {
			trie.children[letter] = &Trie{
				children: make(map[rune]*Trie),
				isLast: false,
			}
		}
		trie = trie.children[letter]
	}
	trie.isLast = true
}

func (this *Trie) Search(word string) bool {
	trie := this
	for _, letter := range word {
		if _, exist := trie.children[letter]; !exist {
			return false
		}
		trie = trie.children[letter]
	}
	
	return trie.isLast
}

func (this *Trie) StartsWith(prefix string) bool {
	trie := this
	for _, letter := range prefix {
		if _, exist := trie.children[letter]; !exist {
			return false
		}
		trie = trie.children[letter]
	}
	return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
