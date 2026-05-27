# data_generation.py

import pandas as pd
import numpy as np

# -----------------------------
# 실제 실험 데이터
# -----------------------------

real_data = {
    "pH": [4, 7, 8, 10],
    "mass": [15.1, 15.2, 15.3, 14.8]
}

df_real = pd.DataFrame(real_data)

# -----------------------------
# 효소 활성도 계산
# 질량 감소량 = 효소 활성
# -----------------------------

m0 = 15.5

df_real["activity"] = m0 - df_real["mass"]

# -----------------------------
# pH 보간(interpolation)
# -----------------------------
# 중간 pH 생성

ph_interp = np.arange(4, 10.1, 0.5)

activity_interp = np.interp(
    ph_interp,
    df_real["pH"],
    df_real["activity"]
)

df_interp = pd.DataFrame({
    "pH": ph_interp,
    "activity": activity_interp
})

# -----------------------------
# 노이즈 기반 데이터 증강
# Monte Carlo Simulation
# -----------------------------

np.random.seed(42)

synthetic_data = []

for _, row in df_interp.iterrows():

    ph = row["pH"]
    activity = row["activity"]

    # 각 pH마다 15개 생성
    for _ in range(15):

        noise = np.random.normal(0, 0.03)

        synthetic_activity = activity + noise

        synthetic_data.append([
            ph,
            synthetic_activity
        ])

# 데이터프레임 생성
df_synthetic = pd.DataFrame(
    synthetic_data,
    columns=["pH", "activity"]
)

# 음수 제거
df_synthetic["activity"] = df_synthetic["activity"].clip(lower=0)

# 저장
df_synthetic.to_csv(
    "enzyme_activity_data.csv",
    index=False
)

print(df_synthetic.head())

print("\n총 데이터 개수:", len(df_synthetic))
print("CSV 저장 완료")