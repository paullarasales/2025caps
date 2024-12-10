from get_user_input import get_user_input
from create_study_schedule import create_study_schedule
from display_schedule import display_schedule
from plot_schedule import plot_schedule

if __name__ == "__main__":
    total_hours = get_user_input()
    study_schedule = create_study_schedule(total_hours)
    display_schedule(study_schedule)
    plot_schedule(study_schedule)