# plot_comparison.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# 데이터
df = pd.read_csv("enzyme_activity_data.csv")

# 모델 로드
model = joblib.load("enzyme_model.pkl")

# 예측용 pH 범위
x_range = np.linspace(4, 10, 300)

x_range_2d = x_range.reshape(-1, 1)

# 예측
y_pred = model.predict(x_range_2d)

# 그래프
plt.figure(figsize=(8,5))

# 산점도
plt.scatter(
    df["pH"],
    df["activity"],
    alpha=0.5,
    label="Synthetic Data"
)

# 회귀 곡선
plt.plot(
    x_range,
    y_pred,
    linewidth=3,
    label="Polynomial Regression"
)

plt.xlabel("pH")
plt.ylabel("Catalase Activity")

plt.title("Catalase Activity Prediction")

plt.legend()
plt.grid(True)

plt.show()