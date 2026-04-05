# charts.py

import matplotlib.pyplot as plt

def plot_room_usage(stats):
    stats["Room Usage"].plot(kind="bar")
    plt.title("Room Usage")
    plt.show()