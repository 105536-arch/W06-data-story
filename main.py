
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 設定資料路徑
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "cleaned_students.csv"
CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# 讀取資料
df = pd.read_csv(DATA_FILE)

# 設定圖表中文字顯示
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False

# 圖表一：各科平均成績
subjects = ["國文", "英文", "數學"]
columns = ["chinese", "english", "math"]
average_scores = [df[column].mean() for column in columns]

plt.figure(figsize=(8, 5))
plt.bar(subjects, average_scores)
plt.title("各科平均成績")
plt.xlabel("科目")
plt.ylabel("平均分數")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(CHART_DIR / "chart01.png", dpi=150)
plt.close()

# 圖表二：讀書時數與數學成績
plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["math"])
plt.title("讀書時數與數學成績")
plt.xlabel("讀書時數")
plt.ylabel("數學成績")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(CHART_DIR / "chart02.png", dpi=150)
plt.close()

# 顯示分析結果
print("各科平均成績：")
for subject, score in zip(subjects, average_scores):
    print(f"{subject}：{score:.1f}")

correlation = df["study_hours"].corr(df["math"])
print(f"\n讀書時數與數學成績的相關係數：{correlation:.2f}")
print("兩張圖表已儲存到 charts 資料夾。")
