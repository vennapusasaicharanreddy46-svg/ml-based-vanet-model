import pandas as pd
import matplotlib.pyplot as plt
import joblib

# =============================
# LOAD RESULTS
# =============================

baseline = pd.read_csv("data/baseline_results.csv")
ml = pd.read_csv("ml_results.csv")

baseline_time = baseline["Average_Travel_Time"][0]
ml_time = ml["Average_Travel_Time"][0]

# =============================
# TRAVEL TIME COMPARISON
# =============================

plt.figure()
plt.bar(["Baseline", "ML-Based"], [baseline_time, ml_time])
plt.title("Average Travel Time Comparison")
plt.ylabel("Time (seconds)")
plt.xlabel("Method")
plt.show()

# =============================
# IMPROVEMENT %
# =============================

improvement = ((baseline_time - ml_time) / baseline_time) * 100

plt.figure()
plt.bar(["Travel Time Improvement"], [improvement])
plt.title("Improvement Percentage")
plt.ylabel("Improvement (%)")
plt.show()

print("Improvement Percentage:", improvement)

# =============================
# FEATURE IMPORTANCE
# =============================

model = joblib.load("ml/congestion_model.pkl")

features = ["Density", "Speed", "Waiting", "Mode"]
importances = model.feature_importances_

plt.figure()
plt.bar(features, importances)
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.xlabel("Features")
plt.show()

print("Graphs Generated Successfully")
