from study_duration_model import StudyDurationModel
study_topics = [
    {"topic": "Mathematics", "difficulty": 3},
    {"topic": "Science", "difficulty": 2},
    {"topic": "History", "difficulty": 4,},
    {"topic": "English", "difficulty": 1}
]

def create_study_schedule(total_hours):
    print("Creating your study schedule....")
    schedule = []
    hours_left = total_hours

    duration_model = StudyDurationModel()

    for topic in study_topics:
        predicted_duration = duration_model.predict_duration(topic["difficulty"])

        if hours_left >= predicted_duration:
            topic["duration"] = predicted_duration
            schedule.append(topic)
            hours_left -= predicted_duration

    return schedule