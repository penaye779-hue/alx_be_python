# daily_reminder.py

import os

# Check if file exists and is not empty
file_name = "daily_reminder.py"
if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
    print(f"Warning: {file_name} does not exist or is empty.")

# Prompt for a single task
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter your task.")

# Prompt for task priority
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid input. Enter high, medium, or low.")

# Prompt for time-bound information
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Enter yes or no.")

# Match Case for task priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:  # This will handle any unexpected priority input (just in case)
        reminder = f"'{task}' has an undefined priority"

# If statement to modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
