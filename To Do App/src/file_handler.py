import json

FILE_PATH = "data/tasks.txt"


def save_tasks(tasks):

    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():

    try:
        with open(FILE_PATH, "r") as file:

            data = file.read()

            if data.strip() == "":
                return []

            return json.loads(data)

    except FileNotFoundError:
        return []