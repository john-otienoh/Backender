# import argparse

# parser = argparse.ArgumentParser(
#     prog="Basic CLI Task App",
#     description="Basic CLI Task App",

# )
# parser.add_argument('filename')
# parser.add_argument('description')
# parser.add_argument('-c', '--count')
# parser.add_argument('-v', '--verbose', action='store_true')
# args = parser.parse_args()

# if args.filename == 'add':
#     print(f"Adding task {args.description}")
#     print(type(args.description))
# print(args.filename,  args.count, args.verbose)

import cmd, sys
from datetime import datetime
from task_manager import save_task, get_tasks

class Task(cmd.Cmd):
    """Interactive Task Tracker Shell"""

    intro = "Welcome to your Basic CLI Task Manager"
    prompt = '(task) '
    file = None

    def __init__(self):
        """Intializer Method"""
        super().__init__()
        self.all_tasks = get_tasks()

    def do_list(self, arg):
        """Lists all tasks: list"""
        print(self.all_tasks)
    
    def do_add(self, arg, status='todo'):
        """Add a new task: add task_name task_status"""
        args = arg.split(maxsplit=1)
        if not args:
            print("Error: Task description required")
            return
        elif len(args) == 1:
            status = args[1]
        elif len(args) > 1:
            print("Error: Expected only two arguments")

        new_task = {
            "ID": len(self.all_tasks) + 1,
            "DESCRIPTION": args[0],
            "STATUS": status,
            "CREATED AT": datetime.now().isoformat(),
            "UPDATED AT": datetime.now().isoformat()
        }

        self.all_tasks.append(new_task)
        save_task(self.all_tasks)
        print(f"Task ID {new_task['ID']} added successfully")

    def do_task(self, task_id):
        tasks = get_tasks()
        for task in tasks:
            if task["ID"] == task_id:
                return task
        return f"Task With ID {task_id} Not Found"

    def do_task(self, task_id, new_description=None, status=None):
        try:
            tasks = get_tasks()
            for task in tasks:
                if task['ID'] == task_id:
                    if new_description is not None:
                        task['DESCRIPTION'] = new_description
                        task['UPDATED AT'] = datetime.now().isoformat()
                        save_task(tasks)
                    if status is not None:
                        task['STATUS'] = new_description
                        task['UPDATED AT'] = datetime.now().isoformat()
                        save_task(tasks)

            print(f"Task With ID {task_id} Not Found")

        except Exception as e:
            print(e)

    def do_delete(self, task_id):
        try:
            tasks = get_tasks()
            for task in tasks:
                if task['ID'] == task_id:
                    tasks.remove(task)
                    save_task(tasks)
                    return f"Task With ID {task_id} deleted successfully"
            print(f"Task With ID {task_id} Not Found")
        except Exception as e:
            print(e)

    def do_bye(self, arg):
        """Exiting the Task App"""
        print("Thank You for using Task CLI App")
        self.close()
        # bye()
        return True
    

    def close(self):
        if self.file:
            self.file.close()
            self.file =None

if __name__ == '__main__':
    Task().cmdloop()
