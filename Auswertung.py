import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("loadtimes.csv")
Modes = sorted(df.Mode.unique())
URLs = df.URL.unique()
df1 = df.loc[(df.Mode == "A") | (df.Mode == "D")]
df2 = df.loc[(df.Mode == "B") | (df.Mode == "E")]
df3 = df.loc[(df.Mode == "C")]
dd = [df.loc[df.URL == url] for url in URLs]

Median = [[d.loc[d.Mode == "A"].median() for d in dd],
          [d.loc[d.Mode == "B"].median() for d in dd],
          [d.loc[d.Mode == "C"].median() for d in dd],
          [d.loc[d.Mode == "D"].median() for d in dd],
          [d.loc[d.Mode == "E"].median() for d in dd]]

Per7 = [[d.loc[d.Mode == "A"].quantile(0.7) for d in dd],
        [d.loc[d.Mode == "B"].quantile(0.7) for d in dd],
        [d.loc[d.Mode == "C"].quantile(0.7) for d in dd],
        [d.loc[d.Mode == "D"].quantile(0.7) for d in dd],
        [d.loc[d.Mode == "E"].quantile(0.7) for d in dd]]

Per3 = [[d.loc[d.Mode == "A"].quantile(0.3) for d in dd],
        [d.loc[d.Mode == "B"].quantile(0.3) for d in dd],
        [d.loc[d.Mode == "C"].quantile(0.3) for d in dd],
        [d.loc[d.Mode == "D"].quantile(0.3) for d in dd],
        [d.loc[d.Mode == "E"].quantile(0.3) for d in dd]]

sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df1, split=True)
plt.savefig("ViolinPlot1.png", dpi=500)
plt.close()
sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df2, split=True)
plt.savefig("ViolinPlot2.png", dpi=500)
plt.close()
sns.violinplot(x="Loading_Time", y="URL", data=df3)
plt.savefig("ViolinPlot3.png", dpi=500)
plt.close()
with open("results.txt", "w+") as results:
    results.write("Median:\n")
    for index,rl in enumerate(URLs):
        results.write(f"URL: {rl} \n")
        for i in range(len(Modes)):
            results.write(f"{Modes[i]}: {Median[i][index]}\n")
    results.write("70th Percentile:\n")
    for index,rl in enumerate(URLs):
        results.write(f"URL: {rl} \n")
        for i in range(len(Modes)):
            results.write(f"{Modes[i]}: {Per7[i][index]}\n")
    results.write("50th Percentile:\n")

    for index, rl in enumerate(URLs):
        results.write(f"URL: {rl} \n")
        for i in range(len(Modes)):
            results.write(f"{Modes[i]}: {Per3[i][index]}\n")
