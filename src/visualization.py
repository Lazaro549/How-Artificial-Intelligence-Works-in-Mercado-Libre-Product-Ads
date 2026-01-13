import pandas as pd
import matplotlib.pyplot as plt

def plot_acos_trend(df):
    plt.plot(df["current_acos"])
    plt.title("ACOS Trend Over Time")
    plt.xlabel("Campaign")
    plt.ylabel("ACOS (%)")
    plt.show()
