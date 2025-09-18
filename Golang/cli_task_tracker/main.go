package main

import (
	"flag"
	"fmt"
	"main/utils"
	"os"
	"strconv"
)

func main() {
	flag.Usage = utils.HelpText
	if len(os.Args) == 1 {
		flag.Usage()
		return
	}
	command := os.Args[1]
	tasks, err := utils.LoadTasks()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	switch command {
	case "add":
		if len(os.Args) < 3 {
			fmt.Println("Error: missing task description")
			return
		}
		tasks, task := utils.AddTask(tasks, os.Args[2])
		if err := utils.SaveTasks(tasks); err != nil {
			fmt.Println("Error:", err)
			return
		}
		fmt.Printf("Task added successfully (ID: %d)\n", task.ID)
	case "update":
		if len(os.Args) < 4 {
			fmt.Println("Error: missing arguments for update")
			return
		}
		id, _ := strconv.Atoi(os.Args[2])
		tasks, err = utils.UpdateTask(tasks, id, os.Args[3])
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		utils.SaveTasks(tasks)
		fmt.Println("Task updated successfully")
	case "delete":
		if len(os.Args) < 3 {
			fmt.Println("Error: missing task ID")
			return
		}
		id, _ := strconv.Atoi(os.Args[2])
		tasks, err = utils.DeleteTask(tasks, id)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		utils.SaveTasks(tasks)
		fmt.Println("Task deleted successfully")
	case "mark-in-progress":
		if len(os.Args) < 3 {
			fmt.Println("Error: missing task ID")
			return
		}
		id, _ := strconv.Atoi(os.Args[2])
		tasks, err = utils.MarkTask(tasks, id, utils.StatusInProgress)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		utils.SaveTasks(tasks)
		fmt.Printf("Task %d marked as in-progress\n", id)
	case "mark-done":
		if len(os.Args) < 3 {
			fmt.Println("Error: missing task ID")
			return
		}
		id, _ := strconv.Atoi(os.Args[2])
		tasks, err = utils.MarkTask(tasks, id, utils.StatusDone)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		utils.SaveTasks(tasks)
		fmt.Printf("Task %d marked as done\n", id)
	case "list":
		filter := ""
		if len(os.Args) > 2 {
			filter = os.Args[2]
		}
		utils.ListAllTasks(tasks, filter)
	default:
		flag.Usage = utils.HelpText
		flag.Usage()
	}

}
