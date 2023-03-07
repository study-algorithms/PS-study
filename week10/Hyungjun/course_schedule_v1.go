func canFinish(numCourses int, prerequisites [][]int) bool {
    g := make([][]int, numCourses)
    for i := 0; i < numCourses; i++ {
        g[i] = make([]int, numCourses)
    }

    for _, pr := range prerequisites {
        a,b := pr[0], pr[1]
        g[b][a] = 1
    }
    skip := []int{}
    for i := 0; i < numCourses; i++ {
        result, s := isClosed(g, i, []int{i}, skip)
        if result == false {
            return false
        }
        skip = s
    }
    return true
}

func isClosed(g [][]int, i int, visited, skip []int) (bool, []int) {
    for j := 0; j < len(g); j++ {
        if g[i][j] == 1 && contains(skip, j) == false {
            if exist := contains(visited, j); exist {
                return false, skip
            }
            _visited := append(visited, j)
            result, s := isClosed(g, j, _visited, skip)
            skip = s 
            if result == false {
                return false, skip
            }
        }
    }
    skip = append(skip, i)
    return true, skip
}

func contains(s []int, i int) bool {
    for _, a := range s {
        if a == i {
            return true
        }
    }
    return false
}
