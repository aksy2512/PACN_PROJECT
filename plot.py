import matplotlib.pyplot as plt
import json

# Path to your JSON data file
file_path = "data.json"

# Load data from JSON file
with open(file_path, "r") as file:
    data = json.load(file)

# Function to plot data for a specific metric (same as before)
def plot_metric(category, metric, ax):
    for filename, values in data[category].items():
        ax.plot(values[metric], label=filename)
    ax.set_title(f"{metric} for {category}")
    ax.set_xlabel("Trial")
    ax.set_ylabel(metric)
    ax.legend()

# Create a figure with subplots for each metric (same as before)
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 12))

# Plot packet loss (same as before)
plot_metric("movement_of_nodes", "packet_loss", axes[0])
plot_metric("no_of_nodes", "packet_loss", axes[0])
plot_metric("traffic", "packet_loss", axes[0])

# Plot delay (same as before)
plot_metric("movement_of_nodes", "delay", axes[1])
plot_metric("no_of_nodes", "delay", axes[1])
plot_metric("traffic", "delay", axes[1])

# Plot throughput (same as before)
plot_metric("movement_of_nodes", "throughput", axes[2])
plot_metric("no_of_nodes", "throughput", axes[2])
plot_metric("traffic", "throughput", axes[2])

plt.tight_layout()
plt.show()
