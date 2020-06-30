import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sns.set_style("whitegrid")
speicherart = 1

df = pd.read_csv("~/Python/check-website-speed/loadtimes.csv")
df1 = df.loc[(df.Mode == "A") | (df.Mode == "D")]
df2 = df.loc[(df.Mode == "B") | (df.Mode == "E")]
df3 = df.loc[(df.Mode == "C") | (df.Mode == "F")]

A_AVG = df.loc[df.Mode == "A"].Loading_Time.median()
B_AVG = df.loc[df.Mode == "B"].Loading_Time.median()
C_AVG = df.loc[df.Mode == "C"].Loading_Time.median()
D_AVG = df.loc[df.Mode == "D"].Loading_Time.median()
E_AVG = df.loc[df.Mode == "E"].Loading_Time.median()
F_AVG = df.loc[df.Mode == "F"].Loading_Time.median()
ticks = np.array([i for i in range (0,25,2)])/10
sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df1, cut=0, split=True, inner=None, linewidth=0)
plt.title(f"A: {A_AVG}; D: {D_AVG}")
plt.xticks(ticks)
plt.savefig("A&D.svg")
plt.close()
sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df2, cut=0, split=True, inner=None, linewidth=0)
plt.title(f"B: {B_AVG}; E: {E_AVG}")
plt.xticks(ticks)
plt.savefig("B&E.svg")
plt.close()
sns.violinplot(x="Loading_Time", y="URL", hue="Mode", data=df3, cut=0, split=True,inner=None,  linewidth=0)
plt.title(f"C: {C_AVG}; F: {F_AVG}")
plt.xticks(ticks)
plt.savefig("C&F.svg")
