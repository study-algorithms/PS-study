mport (
	"container/heap"
)

type NumFreq struct {
	Num   int
	Freq  int
}

type NumFreqHeap []NumFreq

func (h NumFreqHeap) Len() int           { return len(h) }
func (h NumFreqHeap) Less(i, j int) bool { return h[i].Freq < h[j].Freq }
func (h NumFreqHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *NumFreqHeap) Push(x interface{}) {
	*h = append(*h, x.(NumFreq))
}

func (h *NumFreqHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, num := range nums {
		freqMap[num]++
	}

	h := &NumFreqHeap{}
	for num, freq := range freqMap {
		heap.Push(h, NumFreq{Num: num, Freq: freq})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	result := make([]int, k)
	for i := k - 1; i >= 0; i-- {
		result[i] = heap.Pop(h).(NumFreq).Num
	}

	return result
}
