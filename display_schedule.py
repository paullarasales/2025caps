def display_schedule(schedule):
    print("\nYour Study Schedule:")
    for item in schedule:
        print(f"Topic: {item['topic']}, Difficulty: {item['difficulty']}, Duration: {item['duration']} hours")
