def get_user_input():
    print("Welcome to the Study Planner!")

    while True:
        user_input = input("Enter the total hours available for study: ")

        try:
            total_hours = float(user_input)
            if total_hours <= 0:
                print("Please enter a positive number for hours.")
            else:
                return total_hours
        except ValueError:
            print("Invalid input! Please enter a valid number.")