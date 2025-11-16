# daily_reminder.py

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

# Build the customized reminder using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the final customized reminder
print(reminder)
