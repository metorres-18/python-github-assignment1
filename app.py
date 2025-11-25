print("Welcome to the subject Study Tracker!")
# Collecting Users infromation
student_name = input("What is your name? ")
subject = input("What subject did you study? ")
hours = input("How many hours did you study? ")

    # ensure numeric and calculate minutes and progress toward a weekly goal
hours = float(hours)
minutes = int(hours * 60)
weekly_goal = 10.0
remaining = max(0.0, weekly_goal - hours)

print(f"You studied for {minutes} minutes.")
if remaining == 0.0:
    print("You've reached your weekly study goal!")
else:
    print(f"You need {remaining:.1f} more hours to reach a {weekly_goal:.0f}-hour weekly goal.")