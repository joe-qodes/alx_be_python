task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter: high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()


match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task"
    case "medium":
        reminder = f"'{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"'{task}' is a LOW priority task"
    case _:
        reminder = f"'{task}' is a task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."


print("\nReminder:", reminder)
