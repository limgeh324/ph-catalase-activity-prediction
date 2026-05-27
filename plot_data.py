# plot_data.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("enzyme_activity_data.csv")

plt.figure(figsize=(8,5))

plt.scatter(
    df["pH"],
    df["activity"],
    alpha=0.6
)

plt.xlabel("pH")
plt.ylabel("Catalase Activity")

plt.title("pH vs Catalase Activity")

plt.grid(True)

plt.show()