import matplotlib.pyplot as plt
from data_handling.data_loader import load_ieeg_data, load_events_data, load_beh_data, load_experiment_setting_data
from data_handling.behavioral_events import plot_behavioral_events, visualize_word_repetitions, analyze_list_increments
from data_handling.electrodes_position import visualize_electrodes_position

output_dir = "output"

def main():
    ieeg_data = load_ieeg_data()
    events_data = load_events_data()
    beh_data = load_beh_data()
    experiment_setting_data = load_experiment_setting_data()

    # plot_behavioral_events(events_data, output_dir)
    # visualize_electrodes_position(experiment_setting_data, output_dir)
    
    # print(events_data)
    
    analyze_list_increments(events_data)

    # trial_numbers = events_data['list'].unique()

    # # Create visualizations for all trials
    # for trial_num in trial_numbers:
    #     fig = visualize_word_repetitions(events_data, trial_num)
    #     fig.savefig(f'word_repetitions_trial_{trial_num}.png')
    #     plt.close(fig)
        
    return

if __name__ == "__main__":
    main()