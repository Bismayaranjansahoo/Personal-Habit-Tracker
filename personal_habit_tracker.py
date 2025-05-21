
import json
import os
from datetime import datetime

DATA_FILE = 'habit_data.json'

def load_data():
    """Load habit data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    """Save habit data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def log_habit(habit_name):
    """Log a habit completion for today."""
    data = load_data()
    date_today = datetime.now().strftime('%Y-%m-%d')
    if habit_name not in data:
        data[habit_name] = {'goal': 0, 'log': {}}
    data[habit_name]['log'][date_today] = True
    save_data(data)
    print(f"Logged habit: {habit_name} for {date_today}")

def view_progress(habit_name):
    """View progress for a specific habit."""
    data = load_data()
    if habit_name not in data:
        print("Habit not found.")
        return

    habit_data = data[habit_name]
    log_data = habit_data['log']
    total_days = len(log_data)
    completed_days = sum(1 for completed in log_data.values() if completed)
    goal = habit_data['goal']

    completion_rate = (completed_days / total_days * 100) if total_days > 0 else 0
    print(f"\nProgress for '{habit_name}':")
    print(f"Total days logged: {total_days}")
    print(f"Days completed: {completed_days}")
    print(f"Completion rate: {completion_rate:.2f}%")
    print(f"Goal: {goal} days")
    
    
    if completed_days >= goal and goal > 0:
        print("Congratulations! Goal achieved.")
    elif goal > 0:
        print("Goal not yet achieved.")

def set_goal(habit_name, goal_days):
    """Set a goal for a specific habit."""
    data = load_data()
    if habit_name not in data:
        data[habit_name] = {'goal': goal_days, 'log': {}}
    else:
        data[habit_name]['goal'] = goal_days
    save_data(data)
    print(f"Set goal of {goal_days} days for habit: {habit_name}")

def generate_report():
    """Generate a summary report of all habits."""
    data = load_data()
    print("\nHabit Tracker Report:")
    for habit_name, habit_data in data.items():
        log_data = habit_data['log']
        total_days = len(log_data)
        completed_days = sum(1 for completed in log_data.values() if completed)
        goal = habit_data['goal']
        completion_rate = (completed_days / total_days * 100) if total_days > 0 else 0
        
        print(f"\nHabit: {habit_name}")
        print(f"Total days logged: {total_days}")
        print(f"Days completed: {completed_days}")
        print(f"Completion rate: {completion_rate:.2f}%")
        print(f"Goal: {goal} days")
        if completed_days >= goal and goal > 0:
            print("Goal achieved.")
        elif goal > 0:
            print("Goal not yet achieved.")

def main():
    """Main menu for the Habit Tracker application."""
    while True:
        print("\nHabit Tracker")
        print("1. Log Habit")
        print("2. View Progress")
        print("3. Set Goal")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            habit_name = input("Enter habit name: ").strip()
            log_habit(habit_name)
        elif choice == '2':
            habit_name = input("Enter habit name to view progress: ").strip()
            view_progress(habit_name)
        elif choice == '3':
            habit_name = input("Enter habit name to set goal: ").strip()
            try:
                goal_days = int(input("Enter number of days for goal: ").strip())
                if goal_days < 0:
                    raise ValueError("Goal days cannot be negative.")
                set_goal(habit_name, goal_days)
            except ValueError as e:
                print(f"Invalid input: {e}")
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
