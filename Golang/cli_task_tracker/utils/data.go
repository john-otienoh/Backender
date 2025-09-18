package utils

import (
	"encoding/json"
	"fmt"
	"os"
)

const fileName = "tasks.json"

func LoadTasks() ([]Task, error) {
	_, err := os.Stat(fileName)
	if err != nil {
		if os.IsNotExist(err) {
			return []Task{}, nil
		}
		return nil, fmt.Errorf("error checking file: %v", err)
	}

	data, err := os.ReadFile(fileName)
	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	var tasks []Task
	unmarshalErr := json.Unmarshal(data, &tasks)

	if unmarshalErr != nil {
		return nil, fmt.Errorf("error parsing JSON: %v", unmarshalErr)
	}
	return tasks, nil
}

func SaveTasks(tasks []Task) error {
	data, err := json.MarshalIndent(tasks, "", "  ")
	if err != nil {
		return fmt.Errorf("error encoding json: %v", err)
	}

	if err := os.WriteFile(fileName, data, 0644); err != nil {
		return fmt.Errorf("error writing file: %v", err)
	}
	return nil
}
