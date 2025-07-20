# daily_reminder.py

# Prompt for task input
task = input("Enter your task: ").strip()

# Input validation loop for priority
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter a valid priority: high, medium, or low.")

# Input validation loop for time sensitivity
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ("yes", "no"):
        break
    print("Please enter yes or no.")

# Process the task using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task. Try to address it soon."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Add time-bound urgency if applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Output the final reminder
print("\n" + reminder)

