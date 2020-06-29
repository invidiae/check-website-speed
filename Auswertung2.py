import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_style("whitegrid")

df = pd.read_csv("~/Dokumente/check-website-speed/loadtimes.csv")
df1 = df.loc[(df.Mode == "A") | (df.Mode == "D")]
df2 = df.loc[(df.Mode == "B") | (df.Mode == "E")]
df3 = df.loc[(df.Mode == "C")]

fig, ax = plt.subplots(nrows=3, ncols=1)
sns.violinplot(x="Loading_Time", y="Mode", hue="URL", data=df1, ax=ax[0])
sns.violinplot(x="Loading_Time", y="Mode", hue="URL", data=df2, ax=ax[1])
sns.violinplot(x="Loading_Time", y="Mode", hue="URL", data=df3, ax=ax[2])
plt.savefig("superplot_low_dpi.png")
