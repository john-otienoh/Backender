import json
from datetime import datetime
from contextlib import contextmanager
import os
from typing import Union, Dict, TextIO, List
# from tabulate import tabulate


@contextmanager
def task_file_manager(mode: str = 'r') -> Union[List[Dict], TextIO, None]:
    try:
        if not os.path.exists('tasks.json'):
            with open('tasks.json', mode='w', encoding='utf-8') as file:
                json.dump([], file)

        with open('tasks.json', mode=mode, encoding='utf-8') as file:
            if mode == 'r':
                try:
                    yield json.load(file)
                except json.JSONDecodeError:
                    yield []
            else:
                yield file
    except IOError:
        yield None

def get_tasks():
    with task_file_manager() as tasks:
        return tasks if tasks is not None else []
    
def save_task(tasks):
    with task_file_manager(mode='w') as file:
        if file is None:
            return False
        json.dump(tasks, file, indent=4)
        return True


if __name__ == '__main__':
    data = get_tasks()
    print(data)
