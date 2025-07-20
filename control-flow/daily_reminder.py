task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority not in ['high', 'medium', 'low']:
    print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
else:
    if time_bound not in ['yes', 'no']:
        print("Invalid response for time-bound. Please enter 'yes' or 'no'.")
    else:
        match priority:
            case 'high':
                reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention!"
            case 'medium':
                reminder = f"Reminder: '{task}' is a medium priority task. Try to complete it soon."
            case 'low':
                reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."

        if time_bound == 'yes':
            reminder += " Don't forget, it needs to be done today!"

        print("Reminder:", reminder)
