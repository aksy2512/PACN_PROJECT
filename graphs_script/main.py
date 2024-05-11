import json
import matplotlib.pyplot as plt

def plot_graphs(data, title, save_filename=None):
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    fig.suptitle(title, fontsize=16)

    for i, metric in enumerate(['packet_loss', 'delay', 'throughput']):
        ax = axes[i]
        ax.set_title(metric.capitalize())
        for filename, values in data.items():
            ax.plot(values[metric], label=filename)
        ax.set_xlabel('Measurement')
        ax.set_ylabel(metric.capitalize())
        ax.legend()
        ax.grid(True)

    plt.tight_layout()
    if save_filename:
        plt.savefig(save_filename)
    plt.show()

def main():
    with open('../data.json') as f:
        json_data = json.load(f)

    for category, values in json_data.items():
        save_filename = category.replace(' ', '_') + '.png'
        plot_graphs(values, title=category, save_filename=save_filename)

if __name__ == "__main__":
    main()
