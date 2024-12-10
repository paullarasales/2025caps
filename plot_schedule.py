import matplotlib.pyplot as plt

def plot_schedule(schedule):
    topics = [item['topic'] for item in schedule]
    durations = [item['duration'] for item in schedule]

    plt.bar(topics, durations)
    plt.xlabel('Topics')
    plt.ylabel('Study Durations (hours)')
    plt.title('Study Plan')
    plt.show()

    