import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("loadtimes.csv")
Modes = ["A", "B", "C", "D", "E"]
avgs = {}
for M in Modes:
    avgs[M] = (df.loc[df["Mode"] == M].Loading_Time.median())
ninety_per = {}
for M in Modes:
    ninety_per[M] = (df.loc[df["Mode"] == M].Loading_Time.quantile(0.95))
ten_per = {}
for M in Modes:
    ten_per[M] = (df.loc[df["Mode"] == M].Loading_Time.quantile(0.1))


sns.violinplot(df.Loading_Time, df.Mode)
plt.savefig("ViolinPlot.png")

with open("results.txt", "w+") as results:
    results.write("Median: \n")
    for avg in avgs:
        results.writelines(f"{avg}: {avgs[avg]}\n")

    results.write("95th percentile: \n")
    for p in ninety_per:
        results.writelines(f"{p}: {ninety_per[p]}\n")
    results.write("10th percentile:\n")
    for p in ten_per:
        results.writelines(f"{p}: {ten_per[p]}\n")
