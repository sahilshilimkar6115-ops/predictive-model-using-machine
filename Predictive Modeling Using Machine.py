# Predictive Modeling Using Machine Learning
# Zero External Libraries - Only Python Built-in
# Simple Decision Tree logic using basic math

import random

print("Predictive Modeling Using Machine Learning")
print("=" * 50)


# Features: [study_hours, attendance_%]
data = [
    [5, 80, 1], [2, 60, 0], [8, 90, 1], [1, 50, 0], [7, 85, 1],
    [3, 65, 0], [9, 95, 1], [4, 70, 1], [2, 55, 0], [6, 88, 1],
    [5, 75, 1], [3, 62, 0], [8, 92, 1], [1, 45, 0], [7, 82, 1],
    [4, 68, 0], [9, 96, 1], [2, 58, 0], [6, 80, 1], [5, 78, 1]
]


random.seed(42)
random.shuffle(data)
split = int(0.7 * len(data))
train_data = data[:split]
test_data = data[split:]

print(f"Total samples: {len(data)}")
print(f"Training samples: {len(train_data)}")
print(f"Testing samples: {len(test_data)}")


# Rule: if study_hours >= 4 AND attendance >= 70 then Pass = 1
def predict(hours, attendance):
    if hours >= 4 and attendance >= 70:
        return 1
    else:
        return 0

correct = 0
true_positive = 0
false_positive = 0
false_negative = 0
true_negative = 0

print("\nTest Results:")
print("Hours | Attendance | Actual | Predicted")
print("-" * 40)

for row in test_data:
    hours, attendance, actual = row
    predicted = predict(hours, attendance)
    
    print(f" {hours} | {attendance} | {actual} | {predicted}")
    
    if predicted == actual:
        correct += 1
    
    # Confusion matrix sathi
    if actual == 1 and predicted == 1:
        true_positive += 1
    elif actual == 0 and predicted == 1:
        false_positive += 1
    elif actual == 1 and predicted == 0:
        false_negative += 1
    else:
        true_negative += 1


accuracy = correct / len(test_data) * 100

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)
print(f"Accuracy: {round(accuracy, 2)} %")


print("\nConfusion Matrix:")
print(" Predicted")
print(" Fail Pass")
print(f"Actual Fail {true_negative} {false_positive}")
print(f" Pass {false_negative} {true_positive}")

if true_positive + false_positive > 0:
    precision = true_positive / (true_positive + false_positive)
else:
    precision = 0
    
if true_positive + false_negative > 0:
    recall = true_positive / (true_positive + false_negative)
else:
    recall = 0

print(f"\nPrecision: {round(precision, 2)}")
print(f"Recall: {round(recall, 2)}")

print("\nExpected Outcome: Gain experience in supervised learning and model evaluation")
print("=" * 50)