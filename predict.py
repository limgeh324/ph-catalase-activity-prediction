# predict.py

import numpy as np
import joblib

# 모델 로드
model = joblib.load("enzyme_model.pkl")

# 입력
ph = float(input("예측할 pH 입력: "))

# 예측
prediction = model.predict(
    np.array([[ph]])
)

print(f"\npH {ph} 에서의 예상 효소 활성도:")
print(round(prediction[0], 4))