// Not solved -> Timeout

type Edge struct {
	Node   int
	Weight int
}

type Graph map[int][]Edge

func solution(n int, paths [][]int, gates []int, summits []int) []int {
	graph := Graph{}
	for _, path := range paths {
		node1, node2, dist := path[0], path[1], path[2]
		if _, exist := graph[node1]; !exist {
			graph[node1] = []Edge{
				{node2, dist},
			}
		} else {
			graph[node1] = append(graph[node1], Edge{node2, dist})
		}
		if _, exist := graph[node2]; !exist {
			graph[node2] = []Edge{
				{node1, dist},
			}
		} else {
			graph[node2] = append(graph[node2], Edge{node1, dist})
		}
	}
	total_minIntensity := 1000000001
	total_summit := 0
	for _, summit := range summits {
		outer_minIntensity := 1000000001
		for _, gate := range gates {
			routes := [][]int{}
			traverse(graph, summit, gate, make(map[int]bool), []int{}, &routes, gates, summits)
			inner_minIntensity := 1000000001
			for _, route := range routes {
				if intensity := findMax(route); intensity < inner_minIntensity {
					inner_minIntensity = intensity
				}
			}
			if inner_minIntensity < outer_minIntensity {
				outer_minIntensity = inner_minIntensity
			}
		}
		if outer_minIntensity < total_minIntensity {
			total_minIntensity = outer_minIntensity
			total_summit = summit
		}
	}

	return []int{total_summit, total_minIntensity}
}

func traverse(graph Graph, current, end int, visited map[int]bool, route []int, routes *[][]int, gates []int, summits []int) {
	if current == end {
		*routes = append(*routes, route)
		return
	}
	visited[current] = true

	for _, edge := range graph[current] {
		neighbor := edge.Node
		if !visited[neighbor] && !contains(summits, neighbor) {
			if contains(gates, neighbor){
				if neighbor != end {
					continue
				}
			}
			traverse(graph, neighbor, end, visited, append(route, edge.Weight), routes, gates, summits)
		}
	}
	visited[current] = false
}

func findMax(sl []int) int {
	if len(sl) == 0 {
		return 0
	}

	max := sl[0]
	for _, num := range sl[1:] {
		if num > max {
			max = num
		}
	}

	return max
}

func contains(sl []int, n int) bool {
	for _, v := range sl {
		if v == n {
			return true
		}
	}
	return false
}
