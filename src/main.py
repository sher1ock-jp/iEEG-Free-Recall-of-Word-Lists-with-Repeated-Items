import matplotlib.pyplot as plt
from data_handling.data_loader import load_ieeg_data, load_events_data, load_beh_data, load_experiment_setting_data
from data_handling.behavioral_events import plot_behavioral_events

output_dir = "output"

def main():
    ieeg_data = load_ieeg_data()
    events_data = load_events_data()
    beh_data = load_beh_data()
    experiment_setting_data = load_experiment_setting_data()

    plot_behavioral_events(events_data, output_dir)
    return

if __name__ == "__main__":
    main()