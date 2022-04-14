\\ solved using a quick and dirty implementation of a trie data structure 
\\ its actually rather slow
func groupAnagrams(strs []string) [][]string {
  type trieNode struct {
    leaf [26]*trieNode
    isEnd bool
  }
  
  type trie struct {
    root *trieNode
  }
    
  list_size := len(strs)
  m := make(map[string][]int)
  result := [][]string{}

  t := &trie{root: &trieNode{}}
  
  for i := 0; i < list_size; i++ {
    word := strs[i]
    word_size := len(word)
    cursor := t.root

    r := []rune(word)
    sort.Slice(r, func(i int, j int) bool { return r[i] < r[j] })

    s := string(r)

    for j := 0; j < word_size; j++ {
      key := s[j] - 'a'
      if cursor.leaf[key] == nil {
        cursor.leaf[key] = &trieNode{}
      }
      cursor = cursor.leaf[key]
      
    }
    cursor.isEnd = true
    if m[s] == nil {
      m[s] = []int{i}
    } else {
		  m[s] = append(m[s], i)
	  }
  }
  
  for _, value := range m {
		var temp []string
		for i := 0; i < len(value); i++ {
			temp = append(temp, strs[value[i]])
		}
		result = append(result, temp)
	}

   return result
}
