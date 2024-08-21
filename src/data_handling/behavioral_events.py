import matplotlib.pyplot as plt
import os
import pandas as pd

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

def analyze_list_increments(events_data, output_file="list_increment_analysis.txt"):
    pd.set_option('display.max_rows', None)
    # print list with word and onset
    print(events_data[['onset', 'item_name', 'list']])

    # # Sort the data by onset time to ensure chronological order
    # events_data_sorted = events_data.sort_values('onset')
    
    # # Initialize variables
    # current_list = None
    # list_start_times = {}
    # list_end_times = {}

    # # Find the start and end times for each list
    # for _, row in events_data_sorted.iterrows():
    #     if row['list'] != current_list:
    #         if current_list is not None:
    #             list_end_times[current_list] = row['onset']
    #         current_list = row['list']
    #         list_start_times[current_list] = row['onset']
    
    # # Add the end time for the last list with the maximum onset time
    # if current_list is not None:
    #     list_end_times[current_list] = events_data_sorted['onset'].max()
    
    # # Open the output file in write mode
    # with open(output_file, "w") as f:
    #     # Write the results to the file
    #     f.write("List Increment Analysis:\n")
    #     for list_num in sorted(list_start_times.keys()):
    #         start_time = list_start_times[list_num]
    #         end_time = list_end_times[list_num]
    #         duration = end_time - start_time
    #         f.write(f"List {list_num}: Start: {start_time:.2f}s, End: {end_time:.2f}s, Duration: {duration:.2f}s\n")
        
    #     # Analyze the events at list transitions
    #     f.write("\nEvents at List Transitions:\n")
    #     for list_num in sorted(list_start_times.keys())[1:]:  # Skip the first list
    #         transition_time = list_start_times[list_num]
    #         events_before = events_data_sorted[
    #             (events_data_sorted['onset'] < transition_time) & 
    #             (events_data_sorted['onset'] > transition_time - 10)
    #         ]
    #         events_after = events_data_sorted[
    #             (events_data_sorted['onset'] >= transition_time) & 
    #             (events_data_sorted['onset'] < transition_time + 10)
    #         ]
    #         f.write(f"\nTransition to List {list_num}:\n")
    #         f.write("Last few events of previous list:\n")
    #         f.write(events_before[['onset', 'trial_type', 'item_name']].tail().to_string(index=False) + "\n")
    #         f.write("\nFirst few events of new list:\n")
    #         f.write(events_after[['onset', 'trial_type', 'item_name']].head().to_string(index=False) + "\n")

    # print(f"Analysis written to {output_file}")

def visualize_word_repetitions(events_data, trial_number):
    trial_data = events_data[(events_data['list'] == trial_number) & (events_data['trial_type'] == 'WORD')]

    # Create a dictionary to store word occurrences with their onset times
    word_occurrences = {}
    for _, row in trial_data.iterrows():
        word = row['item_name']
        if word not in word_occurrences:
            word_occurrences[word] = []
        word_occurrences[word].append(row['onset'])
    
    # Sort words by their first occurrence time
    sorted_words = sorted(word_occurrences.items(), key=lambda x: min(x[1]))
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(15, 10))
    
    for i, (word, times) in enumerate(sorted_words):
        color = plt.cm.tab20(i / len(sorted_words))
        ax.scatter(times, [i] * len(times), label=word, color=color, s=100)
        
        # Draw lines connecting repetitions
        if len(times) > 1:
            ax.plot(times, [i] * len(times), color=color, alpha=0.5)
        
        # Add text labels for onset times
        for time in times:
            ax.text(time, i, f'{time:.2f}s', verticalalignment='bottom', fontsize=8)
    
    ax.set_yticks(range(len(sorted_words)))
    ax.set_yticklabels([word for word, _ in sorted_words])
    ax.set_xlabel('Time (seconds)')
    ax.set_title(f'Word Repetitions in Trial {trial_number} with Presentation Times')
    
    # Set x-axis limits
    ax.set_xlim(min(trial_data['onset']) - 5, max(trial_data['onset']) + 5)
    
    # Add legend
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    return fig
