task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Match Case to handle priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority. Please clarify."

# Add extra note if time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print final reminder
print(f"Reminder:{reminder}")