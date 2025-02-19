class ToDo:
    def __init__(self, todo_list):
        self.todo_list = todo_list

    def get_todo_list(self):
        return self.todo_list

    def set_todo_list(self, todo_list):
        self.todo_list = todo_list

    def add_todo(self, todo, date_todo):
        self.todo_list.append({'todo': todo, 'date_todo': date_todo})

    def delete_todo(self, delete_todo):
        for todo in self.todo_list:
            if todo['todo'] == delete_todo:
                self.todo_list.remove(todo)
