# -------------------------------------------------------------
# DAY 2: Python Data Structures & Control Loops
# -------------------------------------------------------------

# 1. LISTS (Ordered, mutable collections of data)
# In Data Science, lists are often used to store data samples or features.
skills = ["Python", "Git", "SQL", "Pandas", "Scikit-Learn"]
skills.append("PyTorch")  # Adding a new element to the end of list

print("--- Data Science Skills List ---")
for index, skill in enumerate(skills, start=1):
    print(f"Skill {index}: {skill}")

# 2. DICTIONARIES (Key-Value pairs)
# Used heavily for JSON data, API responses, and model hyperparameters.
model_config = {
    "model_name": "RandomForestClassifier",
    "n_estimators": 100,
    "max_depth": 10,
    "is_trained": False
}

print("\n--- Model Configuration Details ---")
for key, value in model_config.items():
    print(f"{key.upper()}: {value}")

# 3. LIST COMPREHENSION (Pythonic way to filter/transform data)
# Imagine these are accuracy scores from different ML experiments:
raw_accuracy_scores = [0.45, 0.78, 0.92, 0.31, 0.88, 0.95]

# Goal: Filter out low scores and keep scores strictly greater than 0.75
high_performance_scores = [score for score in raw_accuracy_scores if score > 0.75]

print(f"\nFiltered High Accuracy Scores (> 0.75): {high_performance_scores}")

# 4. WHILE LOOP (Iterative logic)
# Simulating a basic training loop threshold
epochs_trained = 0
total_target_epochs = 5

print("\n--- Model Training Simulation ---")
while epochs_trained < total_target_epochs:
    epochs_trained += 1
    print(f"Training Epoch {epochs_trained}/{total_target_epochs} completed...")

print("Training finished successfully!")






# PRACTICE TASK: Student Score Filtering
# -------------------------------------------------------------

# 1. Create a list of 5 student scores
student_scores = [60, 85, 40, 90, 75]  

# 2. Filter scores strictly greater than 70 using List Comprehension
passed_scores = [score for score in student_scores if score > 70]

# 3. Print the results
print(f"\nAll Student Scores: {student_scores}")
print(f"Passed Student Scores (> 70): {passed_scores}")
