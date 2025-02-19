import json
import os
from models_v2 import ToDo

filename = 'todo.json'

if not os.path.isfile(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

with open(filename, 'r') as f:
    start_json = json.load(f)

todo_now = ToDo(start_json)


def save_in_file():
    with open(filename, 'w') as json_file:
        json.dump(start_json, json_file)


def add_my_todo(todo_title, todo_date):
    todo_now.add_todo(todo_title, todo_date)


def delete_my_todo(todo_title):
    todo_now.delete_todo(todo_title)


def get_my_todo_list():
    return todo_now.todo_list


if __name__ == '__main__':
    todo_now.add_todo("Покорми кота", "19.02.2025 вечер")

    todo_now.delete_todo("Покорми кота")

    save_in_file()
