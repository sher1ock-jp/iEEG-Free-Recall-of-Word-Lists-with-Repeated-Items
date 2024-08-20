import pandas as pd
import mne


edf_path = "/Users/takayukiono/Desktop/MyProject/neuro/iEEG-Free-Recall-of-Word-Lists-with-Repeated-Items/data/sub-R1204T/ses-0/ieeg/sub-R1204T_ses-0_task-RepFR1_acq-bipolar_ieeg.edf"
events_path = "/Users/takayukiono/Desktop/MyProject/neuro/iEEG-Free-Recall-of-Word-Lists-with-Repeated-Items/data/sub-R1204T/ses-0/ieeg/sub-R1204T_ses-0_task-RepFR1_events.tsv"
beh_path = "/Users/takayukiono/Desktop/MyProject/neuro/iEEG-Free-Recall-of-Word-Lists-with-Repeated-Items/data/sub-R1204T/ses-0/beh/sub-R1204T_ses-0_task-RepFR1_beh.tsv"
experiment_setting_path = "/Users/takayukiono/Desktop/MyProject/neuro/iEEG-Free-Recall-of-Word-Lists-with-Repeated-Items/data/sub-R1204T/ses-0/ieeg/sub-R1204T_ses-0_task-RepFR1_space-MNI152NLin6ASym_electrodes.tsv"

def load_ieeg_data():
    return mne.io.read_raw_edf(edf_path, preload=False)

def load_events_data():
    return pd.read_csv(events_path, sep='\t')

def load_beh_data():
    return pd.read_csv(beh_path, sep='\t')

def load_experiment_setting_data():
    return pd.read_csv(experiment_setting_path, sep='\t')