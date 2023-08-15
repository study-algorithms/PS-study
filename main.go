package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"runtime"
	"strings"
)

type Project struct {
	Name        string
	WeekCount   int
	WeekList    []Week
	MemberList  map[string]bool
	TotalSolved map[string]int
	Solved      int
}

type Week struct {
	Name           string
	WeekMemberList []Member
}

type Member struct {
	Name   string
	Solved int
}

func main() {
	_, filename, _, ok := runtime.Caller(0)
	if !ok {
		fmt.Println("Error: Unable to get caller info")
		return
	}
	sourceDir := filepath.Dir(filename)
	fmt.Println(sourceDir)

	projectList := []Project{}

	projectNames := []string{"project1", "project2"}
	for _, projectName := range projectNames {
		project := Project{Name: projectName, WeekCount: 0, Solved: 0, MemberList: map[string]bool{}, WeekList: []Week{}, TotalSolved: map[string]int{}}
		filepath.WalkDir(sourceDir+"/"+projectName+"/", func(path string, dir os.DirEntry, err error) error {
			if err != nil {
				fmt.Println("Error : ", err)
				return nil
			}
			if dir.IsDir() && strings.Contains(dir.Name(), "week") {
				project.WeekCount++
			}
			if err != nil {
				fmt.Println("Error : ", err)
			}
			return err
		})
		for i := 1; i <= project.WeekCount; i++ {
			source := sourceDir + "/" + projectName + "/" + fmt.Sprintf("week%v", i) + "/"
			week := Week{Name: fmt.Sprintf("week%v", i), WeekMemberList: []Member{}}
			filepath.WalkDir(source, func(path string, dir os.DirEntry, err error) error {
				if err != nil {
					fmt.Println("Error : ", err)
					return nil
				}
				if dir.IsDir() && !strings.Contains(dir.Name(), "week") {
					member := Member{Name: strings.ToLower(dir.Name())}
					if _, exists := project.TotalSolved[member.Name]; !exists {
						project.TotalSolved[member.Name] = 0
					}
					filepath.Walk(source+"/"+dir.Name(), func(path string, info os.FileInfo, err error) error {
						if err != nil {
							return nil
						}
						if isSolvedFile(info.Name()) {
							member.Solved++
							project.Solved++
							project.TotalSolved[member.Name] += 1
						}
						return err
					})
					week.WeekMemberList = append(week.WeekMemberList, member)
				}
				return err
			})
			project.WeekList = append(project.WeekList, week)
		}
		projectList = append(projectList, project)
	}
	if err := writeToREADME(projectList); err != nil {
		return
	}
}

func isSolvedFile(name string) bool {
	if name == "empty.py" || name == "sample.txt" || name == "sample.py" {
		return false
	}
	re := regexp.MustCompile(`\.(py|cc|go|java|cpp|js)$`)
	return re.MatchString(name)
}

func writeToREADME(projectList []Project) error {
	readme, err := os.Create("README.md")
	if err != nil {
		fmt.Println("Error : ", err)
		return err
	}
	defer readme.Close()
	for _, project := range projectList {
		title := fmt.Sprintf("# %s \n", project.Name)
		body := ""
		for _, v := range project.WeekList {
			body += "## " + v.Name + "\n"
			tableHeader := ""
			tableRows := ""
			for _, m := range v.WeekMemberList {
				tableHeader += "| " + m.Name + " "
				tableRows += fmt.Sprintf("| %v ", m.Solved)
			}
			tableHeader += "|\n"
			for i := 0; i < len(v.WeekMemberList); i++ {
				tableHeader += "| --- "
			}
			tableHeader += "|\n"
			tableRows += "|\n"
			body += tableHeader
			body += tableRows
		}
		total := "## Total\n"
		tableHeader := ""
		tableRows := ""
		for name, solved := range project.TotalSolved {
			tableHeader += "| " + name + " "
			tableRows += fmt.Sprintf("| %v ", solved)
		}
		tableHeader += "|\n"
		for i := 0; i < len(project.TotalSolved); i++ {
			tableHeader += "| --- "
		}
		tableHeader += "|\n"
		tableRows += "|\n"
		total += tableHeader
		total += tableRows

		if _, err := readme.WriteString(title); err != nil {
			return nil
		}
		if _, err := readme.WriteString(body); err != nil {
			return nil
		}
		if _, err := readme.WriteString(total); err != nil {
			return nil
		}
	}
	return nil
}
