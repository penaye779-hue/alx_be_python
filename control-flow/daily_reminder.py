# daily_reminder.py

# Prompt for task
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter your task.")

# Prompt for priority
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid input. Enter high, medium, or low.")

# Prompt for time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Enter yes or no.")

# Match-case to handle priority and construct full reminder message
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
