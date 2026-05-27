# regression.py

import pandas as pd
import joblib

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 데이터 불러오기
df = pd.read_csv("enzyme_activity_data.csv")

X = df[["pH"]]
y = df["activity"]

# 2차 다항 회귀
model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

# 학습
model.fit(X, y)

# 저장
joblib.dump(
    model,
    "enzyme_model.pkl"
)

print("모델 학습 완료")