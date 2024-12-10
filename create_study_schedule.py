study_topics = [
    {"topic": "Mathematics", "difficulty": 3, "duration": 2},
    {"topic": "Science", "difficulty": 2, "duration": 1.5},
    {"topic": "History", "difficulty": 4, "duration": 3},
    {"topic": "English", "difficulty": 1, "duration": 1}
]

def create_study_schedule(total_hours):
    print("Creating your study schedule....")
    schedule = []
    hours_left = total_hours

    sorted_topics = sorted(study_topics, key=lambda x: x["difficulty"], reverse=True)

    for topic in sorted_topics:
        if hours_left >= topic["duration"]:
            schedule.append(topic)
            hours_left -= topic["duration"]
    return schedule