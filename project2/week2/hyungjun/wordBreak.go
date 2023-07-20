package main

type Trie struct {
	children map[rune]*Trie
	isLast   bool
}

func Constructor() Trie {
	return Trie{
		children: make(map[rune]*Trie),
		isLast:   false,
	}
}

func (this *Trie) Insert(word string) {
	trie := this
	for _, letter := range word {
		if trie.children[letter] == nil {
			trie.children[letter] = &Trie{
				children: make(map[rune]*Trie),
				isLast:   false,
			}
		}
		trie = trie.children[letter]
	}
	trie.isLast = true
}

func (this *Trie) Search(word string, i int) (result []int) {
	trie := this

	for _, letter := range word {
		if trie.isLast {
			result = append(result, i)
		}
		if _, exist := trie.children[letter]; !exist {
			return
		}
		i += 1
		trie = trie.children[letter]
	}
	if trie.isLast {
		result = append(result, i)
	}
	return
}

func wordBreak(s string, wordDict []string) bool {
	trie := Constructor()
	for _, w := range wordDict {
		trie.Insert(w)
	}
	check := make([]bool, len(s)+1)
	check[0] = true
	for i := 0; i < len(s); i++ {
		if check[i] {
			result := trie.Search(s[i:], 0)
			for _, v := range result {
				check[i+v] = true
			}
		}
	}
	return check[len(s)]
}
