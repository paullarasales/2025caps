from get_user_input import get_user_input
from create_study_schedule import create_study_schedule
from display_schedule import display_schedule
from plot_schedule import plot_schedule

def main():
    while True:
        print("Starting a new session...")
        total_hours = get_user_input()
        print(f"Total hours entered: {total_hours}")
        study_schedule = create_study_schedule(total_hours)
        display_schedule(study_schedule)
        plot_schedule(study_schedule)

        exit_choice = input("Would you like to exit? (yes/no): ").strip().lower()
        print(f"User chose to exit: {exit_choice}")
        if exit_choice == "yes":
            print("Exiting the Study Planner. Goodbye!")
            break


if __name__ == "__main__":
    main()