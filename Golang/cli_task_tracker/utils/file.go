package utils

import (
	"fmt"
	"os"
	"time"
)

func HelpText() {
	usageText :=
		`
		Task CLI - A simple command line task tracker
		Usage:
		  task-cli [command] [arguments]
		Commands:
		  add <description>               Add a new task
		  update <id> <new description>   Update an existing task
		  delete <id>                     Delete a task
		  mark-in-progress <id>           Mark a task as in-progress
		  mark-done <id>                  Mark a task as done
		  list                            List all tasks
		  list todo                       List all tasks with status = todo
		  list in-progress                List all tasks with status = in-progress
		  list done                       List all tasks with status = done
		Other:
		  help                            Show this help message
		  Use "task-cli [command] --help" for more information about a command.
		
	`
	fmt.Fprintf(os.Stderr, "%s\n\n", usageText)
}

// List all task
func ListAllTasks(tasks []Task, filter string) {
	if len(tasks) == 0 {
		fmt.Println("No tasks found.")
	}
	for _, task := range tasks {
		if filter == "" || task.Status == filter {
			fmt.Printf(
				"[%d] %s | %s | created: %s | updated: %s\n",
				task.ID, task.Description, task.Status,
				task.CreatedAt.Format(time.RFC3339),
				task.UpdatedAt.Format(time.RFC3339),
			)
		}
	}
}
func AddTask(tasks []Task, description string) ([]Task, Task) {
	id := 1
	if len(tasks) > 0 {
		id = tasks[len(tasks)-1].ID + 1
	}

	task := Task{
		ID:          id,
		Description: description,
		Status:      StatusTodo,
		CreatedAt:   GetCurrentTime(),
		UpdatedAt:   GetCurrentTime(),
	}
	tasks = append(tasks, task)
	return tasks, task
}
func UpdateTask(tasks []Task, id int, newDescription string) ([]Task, error) {
	for i := range tasks {
		if tasks[i].ID == id {
			tasks[i].Description = newDescription
			tasks[i].UpdatedAt = GetCurrentTime()
			return tasks, nil
		}
	}
	return tasks, fmt.Errorf("task with ID %d not found", id)
}

func DeleteTask(tasks []Task, id int) ([]Task, error) {
	for i := range tasks {
		if tasks[i].ID == id {
			return append(tasks[:i], tasks[i+1:]...), nil
		}
	}
	return tasks, fmt.Errorf("task with ID %d not found", id)
}

func MarkTask(tasks []Task, id int, status string) ([]Task, error) {
	for i := range tasks {
		if tasks[i].ID == id {
			tasks[i].Status = status
			tasks[i].UpdatedAt = time.Now()
			return tasks, nil
		}
	}
	return tasks, fmt.Errorf("task with ID %d not found", id)
}
