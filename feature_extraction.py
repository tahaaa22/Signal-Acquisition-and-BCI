import pandas as pd
import numpy as np
from scipy.signal import welch

# Load EEG dataset
df = pd.read_csv("Filtered_EEG.csv")



# Function to compute Power Spectral Density (PSD)
def compute_psd(signal, fs=250):
    signal = np.asarray(signal)  # Convert to NumPy array

    # Ensure signal is 1D and has enough data points
    if signal.ndim != 1 or len(signal) < 256:
        return np.nan  # Return NaN if data is insufficient

    freqs, psd = welch(signal, fs, nperseg=min(len(signal), 256))
    return np.mean(psd)  # Return the average PSD value


# Extract features
features = []
for col in df.columns[1:-1]:  # Skip 'Time' and 'Eye_State'
    col_data = df[col].dropna().values  # Ensure it's an array, drop NaN values

    features.append({
        f"{col}_mean": np.mean(col_data),
        f"{col}_var": np.var(col_data),
        f"{col}_psd": compute_psd(col_data)  # Pass full column instead of row[col]
    })

# Convert to DataFrame
feature_df = pd.DataFrame(features)
feature_df["Eye_State"] = df["Eye_State"]  # Add labels

# Save extracted features
feature_df.to_csv("EEG_Features_with_Labels.csv", index=False)

print("✅ Feature extraction complete. Data saved as EEG_Features_with_Labels.csv")
