# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ").strip()

# Prompt for task priority with input validation
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Prompt for time sensitivity with input validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Use match-case to create the initial reminder based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task. Try to get it done soon."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Complete it when you have time."

# Add urgency if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print("\n" + reminder)


