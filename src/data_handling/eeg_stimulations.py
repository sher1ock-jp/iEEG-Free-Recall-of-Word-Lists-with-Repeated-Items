import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne
from nilearn.datasets import load_mni152_template
from nilearn.plotting import plot_anat

mne.viz.set_3d_backend('pyvistaqt')  # Or 'mayavi' if you have it installed

def visualize_electrodes_position(experiment_setting_data, output_dir):
    df = pd.DataFrame(experiment_setting_data)

    # Create a dictionary with electrode names and their corresponding coordinates
    ch_pos = {row['name']: [row['x'], row['y'], row['z']] for _, row in df.iterrows()}

    # Create the montage
    montage = mne.channels.make_dig_montage(ch_pos=ch_pos, coord_frame='head')

    # Create an MNE Info object (this usually includes channel types, sample rates, etc.)
    info = mne.create_info(ch_names=list(ch_pos.keys()), sfreq=1000, ch_types='eeg')

    # Set the montage to the info object
    info.set_montage(montage)

    # Visualize electrode positions in head coordinates with blocking
    fig = mne.viz.plot_alignment(info, dig=True, coord_frame='head', block=True)  # Use 'head' instead of 'mri'
    mne.viz.set_3d_view(fig, 200, 70)  # Adjust view angle

    plt.show()  # In some cases, you might still need this depending on your environment