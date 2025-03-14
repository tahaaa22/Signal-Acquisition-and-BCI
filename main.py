import os

# Run Feature Extraction
print("🔹 Running Feature Extraction...")
os.system("python feature_extraction.py")

# Run EEG Visualization
print("🔹 Launching EEG Viewer...")
os.system("python eeg_visualization.py")
