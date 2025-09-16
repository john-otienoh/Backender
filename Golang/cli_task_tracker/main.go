package main

import (
	// "cli"
	"flag"
	"fmt"
	"os"
)

func helpText() {
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

func main() {
	flag.Usage = helpText
	if len(os.Args) == 1 {
		flag.Usage()
		return
	}
}
