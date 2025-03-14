import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def plot_signals():
    file_path = filedialog.askopenfilename()  # Open file dialog
    df = pd.read_csv(file_path)  # Load EEG file

    plt.figure(figsize=(10, 5))
    for col in df.columns[1:]:  # Skip time column
        plt.plot(df["Time"], df[col], label=f"{col} Filtered")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (μV)")
    plt.title("Filtered EEG Signals")
    plt.legend()
    plt.show()


# Create GUI
root = tk.Tk()
root.title("EEG Signal Viewer")

btn = tk.Button(root, text="Open EEG File", command=plot_signals)
btn.pack()

root.mainloop()
