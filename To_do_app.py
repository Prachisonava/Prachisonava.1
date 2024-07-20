import json

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {'title': title, 'description': description, 'status': 'pending'}
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{title}" added successfully!')

# Function to display all tasks
def show_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} - {task['description']} [{task['status']}]")

# Function to mark a task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        tasks[task_index]['status'] = 'completed'
        save_tasks(tasks)
        print(f'Task "{tasks[task_index]["title"]}" marked as completed!')
    except (IndexError, ValueError):
        print('Invalid task number!')

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()