import json
from models import TaskManager


def save_tasks_in_json(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as outfile:
        json.dump(tasks, outfile)


def import_tasks_from_json():
    with open('tasks.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


if __name__ == '__main__':
    created_tasks = import_tasks_from_json()
    task_manager = TaskManager()
    task_manager.set_tasks(created_tasks)

    task_manager.add_task("Сделать ДЗ по школе", "Сделать дз по алгебре и русскому")

    save_tasks_in_json(task_manager.get_tasks())
