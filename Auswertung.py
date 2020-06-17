import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("loadtimes.csv")
plt.scatter(df.Loading_Time, df.Mode)
plt.savefig("Plot.png")