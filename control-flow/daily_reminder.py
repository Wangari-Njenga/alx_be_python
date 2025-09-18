# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += " but it's not time-sensitive."

# Output the customized reminder
print(reminder)
