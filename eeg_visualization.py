import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv("Eye_Detection.csv")

# Choose an EEG channel to visualize
channel = df.columns[1]  # First EEG channel

# Plot the signal over time
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df[channel], label="EEG Signal", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (μV)")
plt.title(f"EEG Signal - {channel}")
plt.legend()
plt.show()
