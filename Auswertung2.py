import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
speicherart = 1

df = pd.read_csv("~/Python/check-website-speed/loadtimes.csv")
df1 = df.loc[(df.Mode == "A") | (df.Mode == "D")]
df2 = df.loc[(df.Mode == "B") | (df.Mode == "E")]
df3 = df.loc[(df.Mode == "C") | (df.Mode == "F")]

A_AVG = df.loc[df.Mode == "A"].median()
B_AVG = df.loc[df.Mode == "B"].median()
C_AVG = df.loc[df.Mode == "C"].median()
D_AVG = df.loc[df.Mode == "D"].median()
E_AVG = df.loc[df.Mode == "E"].median()
F_AVG = df.loc[df.Mode == "F"].median()


if speicherart == 0:
    fig, ax = plt.subplots(nrows=3, ncols=1)
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df1, split=True, ax=ax[0])
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df2, split=True, ax=ax[1])
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df3, ax=ax[2])
    plt.savefig("superplot.png")
elif speicherart == 1:
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df1, cut=0, split=True)
    plt.title(f"A: {A_AVG}; D: {D_AVG}")
    plt.savefig("A&D.png")
    plt.close()
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df2, cut=0, split=True)
    plt.title(f"B: {B_AVG}; E: {E_AVG}")
    plt.savefig("B&E.png")
    plt.close()
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df3, cut=0, split=True)
    plt.title(f"C: {C_AVG}; F: {F_AVG}")
    plt.savefig("C&F.png")
elif speicherart == 2:
    fig, ax = plt.subplots(nrows=3, ncols=1)
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df1, ax=ax[0])
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df2, ax=ax[1])
    sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df3, ax=ax[2])
    plt.savefig("superplotavgs.png")
