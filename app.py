print("Welcome to the Subject Study Tracker!")
# Collecting Users infromation
student_name = input("What is your name? ")
subject = input("What subject did you study? ")
hours = input("How many hours did you study? ")

#This will prevent the program from crashing if the user inputs invalid data
try:
    # calculate minutes and progress toward a weekly goal
    hours = float(hours)
    minutes = int(hours * 60)
    weekly_goal = 10.0
    remaining = max(0.0, weekly_goal - hours)
    # Displays the number of mintues studied and progress toward weekly goal
    print(f"You studied for {minutes} minutes.")
    if remaining == 0.0:
        print("You've reached your weekly study goal!")
    else:
        print(f"You need {remaining:.1f} more hours to reach a {weekly_goal:.0f}-hour weekly goal.")
    #This will tell the user that they entered invalid data, if they didnt put a number
except ValueError:
    print("Please enter a valid number for hours studied.")
    exit()