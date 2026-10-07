# # # task 1 ////:- 
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

#TASK 2 /////  :-


import requests
from bs4 import BeautifulSoup
import csv


URL = "https://quotes.toscrape.com/"


def scrape_titles(url):
    try:
        # Send request to the website
        response = requests.get(url, timeout=10)

        # Raise an error if the request failed
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote elements
        quotes = soup.find_all("span", class_="text")

        titles = []

        for quote in quotes:
            titles.append(quote.get_text(strip=True))

        return titles

    except requests.exceptions.RequestException as e:
        print("Error while accessing the website:", e)
        return []

    except Exception as e:
        print("An unexpected error occurred:", e)
        return []


def save_to_csv(data, filename):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # CSV header
            writer.writerow(["Quote"])

            # Write scraped data
            for item in data:
                writer.writerow([item])

        print(f"Data successfully saved to {filename}")

    except IOError as e:
        print("Error while saving CSV file:", e)


# Main program
print("Starting web scraper...")

data = scrape_titles(URL)

if data:
    print(f"Found {len(data)} items.")

    for item in data:
        print(item)

    save_to_csv(data, "scraped_data.csv")

else:
    print("No data was scraped.")

#TASK 3 /////  :-

import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    try:
        response = requests.get(API_URL, timeout=10)
    
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            print("Invalid response format.")
            return []

        return data

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the API.")

    except requests.exceptions.HTTPError as e:
        print("API returned an HTTP error:", e)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

    except ValueError:
        print("The API returned invalid JSON data.")

    return []


def display_users(users):
    if not users:
        print("No user data available.")
        return

    print("\n______USER INFORMATION_____\n")

    for user in users:
        print(f"ID     : {user['id']}")
        print(f"Name   : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email   : {user['email']}")
        print(f"City    : {user['address']['city']}")
        print("________________________\n")


print("Fetching data from API")

users = fetch_users()

display_users(users)


