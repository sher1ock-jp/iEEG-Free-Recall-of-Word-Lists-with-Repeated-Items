import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sub-R1204T/ses-0/beh/sub-R1204T_ses-0_task-RepFR1_beh.tsv", delimiter='\t')
print("\n-----------------------------------------------------------------------------------------------")
print("Basic Information:")
print(df.info())

plt.figure(figsize=(10, 6))
df['trial_type'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Trial Types')
plt.xlabel('Trial Type')
plt.ylabel('Count')
plt.show()