#TASK 1 /////  :-

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot perform modulus by zero!"
    return a % b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    print("Result:", add(num1, num2))

elif choice == "2":
    print("Result:", subtract(num1, num2))

elif choice == "3":
    print("Result:", multiply(num1, num2))

elif choice == "4":
    print("Result:", divide(num1, num2))

elif choice == "5":
    print("Result:", modulus(num1, num2))

else:
    print("Invalid choice!")

# TASK 2 /////  :-

import random

secret_number = random.randint(1, 100)
max_attempts = 5

print("Number Guessing Game")
print("I have chosen a number between 1 and 100")
print(f"You have {max_attempts} attempts to guess it")

for attempt in range(1, max_attempts + 1):

    guess = int(input(f"\nAttempt {attempt}: Enter your guess:"))

    if guess == secret_number:
        print("HURRY! Congratulations! You guessed the number correctly!")
        break

    elif guess < secret_number:
        print("guess higher!")

    else:
        print("guess lower!")

else:
    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")

#TASK 3 /////  :-

def word_counter(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        words = content.split()

        word_count = len(words)

        print("Total number of words:", word_count)

    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the file name: ")

word_counter(filename)


#TASK 4 /////  :-
import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: The task file is corrupted.")
        return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task: ").strip()

    if not task_name:
        print("Error: Task cannot be empty.")
        return

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- To-Do List ---")

    for i, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['task']} - {status}")

def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Task does not exist.")
            return

        deleted_task = tasks.pop(task_number - 1)

        save_tasks(tasks)

        print(f"Deleted: {deleted_task['task']}")

    except ValueError:
        print("Error: Please enter a valid task number.")

def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Task does not exist.")
            return

        tasks[task_number - 1]["completed"] = True

        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Error: Please enter a valid task number.")

def main():

    tasks = load_tasks()

    while True:

        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice.")


main()
