import matplotlib.pyplot as plt
import os

def plot_behavioral_events(events_data, output_dir):
    plt.figure(figsize=(12, 8))

    for trial_type in events_data['trial_type'].unique():
        subset = events_data[events_data['trial_type'] == trial_type]
        plt.scatter(subset['onset'], [trial_type] * len(subset), label=trial_type, alpha=0.6)

    plt.xlabel('Time (s)')
    plt.ylabel('Trial Type')
    plt.title('Behavioral Events Over Time')
    plt.legend(title='Trial Type')
    plt.grid(True)

    image_path = os.path.join(output_dir, "behavioral_events_over_time.png")
    plt.savefig(image_path)
    plt.show()