# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to handle different priority levels
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level."

# Add additional information if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the final reminder in the expected format
print(f"\nReminder: {reminder}")
