import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mne

def visualize_electrodes_position(experiment_setting_data, output_dir):
    # Extract electrode information
    x = experiment_setting_data['x'].values
    y = experiment_setting_data['y'].values
    z = experiment_setting_data['z'].values
    labels = experiment_setting_data['name'].tolist()  # Convert to list
    
    # Create a montage
    ch_pos = dict(zip(labels, np.column_stack([x, y, z])))
    montage = mne.channels.make_dig_montage(ch_pos=ch_pos, coord_frame='mni_tal')
    
    # Create info object
    info = mne.create_info(ch_names=labels, sfreq=1000, ch_types='seeg')
    info.set_montage(montage)
    
    # Plot the electrodes
    fig = mne.viz.plot_alignment(info, subject='sample', coord_frame='mri',
                                 subjects_dir=None, dig=True, show_axes=True,
                                 surfaces=['brain'])
    
    # Customize the plot
    mne.viz.set_3d_view(fig, azimuth=45, elevation=60)
    
    # Save the figure
    mne.viz.save_3d_figure(fig, f'{output_dir}/electrode_positions_3d.png')

    # Create 2D projections
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    ax1.scatter(x, y)
    ax1.set_xlabel('X'); ax1.set_ylabel('Y')
    ax1.set_title('Top View')
    
    ax2.scatter(x, z)
    ax2.set_xlabel('X'); ax2.set_ylabel('Z')
    ax2.set_title('Front View')
    
    ax3.scatter(y, z)
    ax3.set_xlabel('Y'); ax3.set_ylabel('Z')
    ax3.set_title('Side View')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/electrode_positions_2d.png')
    plt.close()