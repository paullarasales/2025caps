import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model

study_topics = [
    {"topic": "Math", "difficulty": 3, "duration": 2},
    {"topic": "Science", "difficulty": 2, "duration": 1.5},
    {"topic": "History", "difficulty": 4, "duration": 3},
    {"topic": "English", "difficulty": 1, "duration": 1}
]

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

def create_study_schedule(total_hours):
    print("Creating your study schedule...")
    schedule = []
    hours_left = total_hours

    sorted_topics = sorted(study_topics, key=lambda x: x["difficulty"], reverse=True)

    for topic in sorted_topics:
        if hours_left >= topic["duration"]:
            schedule.append(topic)
            hours_left -= topic["duration"]
    
    return schedule

def display_schedule(schedule):
    print("\nYour Study Schedule:")
    for item in schedule:
        print (f"Topic: {item['topic']}, Difficulty: {item['difficulty']}, Duration: {item['duration']} hours")
        
def plot_schedule(schedule):
    topics = [item['topic'] for item in schedule]
    durations = [item['duration'] for item in schedule]

    plt.bar(topics, durations)
    plt.xlabel('Topics')
    plt.ylabel('Study Duration (hours)')
    plt.title('Study Plan')
    plt.show()

if __name__ == "__main__":
    total_hours = get_user_input()
    study_schedule = create_study_schedule(total_hours)
    display_schedule(study_schedule)
    plot_schedule(study_schedule)