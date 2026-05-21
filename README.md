# 📊 Predictive Modeling Using Machine Learning (No External Libraries)

This project demonstrates a simple *supervised learning model* built using pure Python (without any external ML libraries like scikit-learn or pandas).  
It simulates a basic *student performance prediction system (Pass/Fail)* using study hours and attendance.

---

## 🚀 Project Overview

The model predicts whether a student will *Pass (1)* or *Fail (0)* based on:

- Study Hours
- Attendance Percentage

A simple rule-based logic is used instead of advanced ML libraries.

---

## 📁 Dataset

The dataset is manually created with 20 samples:

| Study Hours | Attendance (%) | Result |
|------------|----------------|--------|
| 5 | 80 | 1 |
| 2 | 60 | 0 |
| 8 | 90 | 1 |
| ... | ... | ... |

---

## ⚙️ Workflow

1. Create dataset
2. Shuffle data randomly
3. Split into:
   - 70% Training Data
   - 30% Testing Data
4. Apply rule-based prediction model
5. Evaluate performance

---

## 🧠 Model Logic

The prediction rule:

```python
if study_hours >= 4 and attendance >= 70:
    return 1  # Pass
else:
    return 0  # Fail
