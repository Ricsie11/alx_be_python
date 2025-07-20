# daily_reminder.py

# Prompt for task input
task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Generate reminder message
match priority:
    case "high":
        message = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        message = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        message = f"Reminder: '{task}' is a LOW priority task."
    case _:
        message = f"Reminder: '{task}' has an UNKNOWN priority level."

# Add time sensitivity notice
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Display the customized reminder
print(message)
