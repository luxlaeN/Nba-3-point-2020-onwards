import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load data from a CSV file
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            global df  # Make the dataframe accessible globally
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", f"Data loaded successfully from {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to plot the data
def plot_data():
    if df is not None:
        try:
            # Clear any existing plots
            for widget in plot_frame.winfo_children():
                widget.destroy()

            # Create a new figure
            fig = Figure(figsize=(5, 4), dpi=100)
            ax = fig.add_subplot(111)

            # Example plot: Plot the first two columns of the DataFrame
            ax.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o')

            # Create a canvas for the matplotlib figure
            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot data: {e}")
    else:
        messagebox.showwarning("Warning", "Please load data first")

# Initialize the main window
root = tk.Tk()
root.title("Data Plotter UI")

# Create a frame for the plot
plot_frame = tk.Frame(root)
plot_frame.pack()

# Create buttons for loading data and plotting
load_button = tk.Button(root, text="Load Data", command=load_data)
load_button.pack(pady=5)

plot_button = tk.Button(root, text="Plot Data", command=plot_data)
plot_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()