
task = input("Enter your task: ")


while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    else:
        print("Please enter 'high', 'medium', or 'low'.")

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")


match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time"
    else:
        message += " but it is not time-sensitive"

print("\n" + message)
