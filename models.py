class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):  # Добавил задачу
        self.__tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, title):  # убрал задачу
        self.__tasks = [task for task in self.__tasks if task['title'] != title]

    def mark_as_done(self, title):  # сделал
        for task in self.__tasks:
            if task['title'] == title:
                task['done'] = True
                break

    def show_tasks(self):  # что осталось сделать
        if not self.__tasks:
            print("Задач для выполнения нема")
        else:
            for task in self.__tasks:
                status = "Выполнено" if task['done'] else "Не выполнено"
                print(f"Задача: {task['title']} \nОписание: {task['description']} \nСтатус: {status}\n")

    def __str__(self):  # чтобы когда я просил вывести выводилось строчкой
        return f"Количество задач: {len(self.__tasks)}"

    def get_tasks(self):
        return self.__tasks

    def set_tasks(self, tasks):
        self.__tasks = tasks


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.add_task("Сделать ДЗ по школе", "Сделать дз по алгебре и русскому")
    task_manager.add_task("Сделать ДЗ по айти школе", "Сделать проект и загрузить в майстат")

    task_manager.mark_as_done("Сделать ДЗ по школе")
    task_manager.show_tasks()

    task_manager.remove_task("Сделать ДЗ по школе")  # типо я уже сделал дз по школе и я его не считаю
    task_manager.show_tasks()  # все что осталось сделать

    print(f"{task_manager}\nСПАСИБО ЗА ВНИМАНИЕ К МОЕМУ ТВОРЕНИЮ:)")
