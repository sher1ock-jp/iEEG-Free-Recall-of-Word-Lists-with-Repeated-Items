import mne
import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = "output"

edf_path = "data/sub-R1204T/ses-0/ieeg/sub-R1204T_ses-0_task-RepFR1_acq-bipolar_ieeg.edf"
events_path = "data/sub-R1204T/ses-0/ieeg/sub-R1204T_ses-0_task-RepFR1_events.tsv"
beh_path = "data/sub-R1204T/ses-0/beh/sub-R1204T_ses-0_task-RepFR1_beh.tsv"

ieeg_data = mne.io.read_raw_edf(edf_path, preload=False)
events_data = pd.read_csv(events_path, sep='\t') 
beh_data = pd.read_csv(beh_path, sep='\t')  # content is same as events_data

# print(ieeg_data.info)
    #  bads: []
    #  ch_names: LT1-LT2, LT2-LT3, LT3-LT4, LT4-LT5, LT5-LT6, LT6-LT7, LT7-LT8, ...
    #  chs: 108 EEG
    #  custom_ref_applied: False
    #  highpass: 0.0 Hz
    #  lowpass: 500.0 Hz
    #  meas_date: 2024-08-12 13:50:51 UTC
    #  nchan: 108
    #  projs: []
    #  sfreq: 1000.0 Hz
    #  subject_info: 3 items (dict)

print(events_data)
# print(pd.set_option('display.max_columns', None))z
    #      onset  duration  sample   trial_type  response_time                  stim_file item_name  serialpos  repeats  list experiment  session subject
    #0    0.000     0.008   11048        START            NaN                        NaN       NaN       -999     -999     0     RepFR1        0  R1204T
    #1    0.008   232.234   11056   SESS_START            NaN                        NaN       NaN       -999     -999     0     RepFR1        0  R1204T
    #2  232.242    13.752  243290  TRIAL_START            NaN                        NaN       NaN       -999     -999     0     RepFR1        0  R1204T
    #3  245.994     3.000  257042    COUNTDOWN            NaN                        NaN       NaN       -999     -999     0     RepFR1        0  R1204T
    #4  250.127     1.600  261175         WORD            NaN  wordpools/wordpool_EN.txt      HORN          0        3     0     RepFR1        0  R1204T

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

# print(pd.set_option('display.max_columns', None))
# print(beh_data.head())


# raw = mne.io.read_raw_edf(edf_file, preload=True)

# eeg_data = raw.get_data()
# times = raw.times



# # Print the column names to check if 'onset' exists
# print("Columns in text data:", text_data.columns)

# # Print the first few rows to inspect the data
# print(text_data.head())

# # If 'onset' exists, proceed with sorting
# if 'onset' in text_data.columns:
#     text_data = text_data.sort_values('onset')
# else:
#     print("The 'onset' column was not found in the text data.")
#     # Handle the situation here if 'onset' is missing

# # Define the duration of interest
# duration_of_interest = 1.0  # For example, 1 second after each onset

# aligned_data = []

# if 'onset' in text_data.columns:
#     for _, row in text_data.iterrows():
#         start_time = row['onset']
#         end_time = start_time + duration_of_interest

#         start_sample = raw.time_as_index(start_time)[0]
#         end_sample = raw.time_as_index(end_time)[0]

#         eeg_segment = eeg_data[:, start_sample:end_sample]
#         aligned_data.append({'text': row['item_name'], 'eeg_segment': eeg_segment})

#     # Example Plotting with Markers for Each Text Presentation
#     plt.figure(figsize=(10, 6))
#     plt.plot(times, eeg_data[0, :])  # Example: plotting the first EEG channel

#     for _, row in text_data.iterrows():
#         plt.axvline(x=row['onset'], color='r', linestyle='--')
#         plt.text(row['onset'], max(eeg_data[0, :]), row['item_name'], rotation=45)

#     plt.xlabel('Time (s)')
#     plt.ylabel('EEG Amplitude')
#     plt.title('EEG Time Series with Text Presentation')
#     plt.show()
