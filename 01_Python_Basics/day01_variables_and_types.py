# -------------------------------------------------------------
# DAY 1: Python Basics - Data Types & Logic
# -------------------------------------------------------------

# 1. Core Data Types
student_name = "KAAN"  # string (str)
completed_weeks = 0                        # integer (int)
daily_hours_target = 4.0                   # float
is_committed = True                        # boolean (bool)

print(f"Target Role: {student_name}")
print(f"Daily Commitment: {daily_hours_target} hours | Active Status: {is_committed}\n")

# 2. Control Flow (If / Else Logic)
logged_hours = 4

if logged_hours >= daily_hours_target:
    status = "Daily goal completed successfully!"
elif logged_hours > 0:
    status = "Partial progress made. Need more focus."
else:
    status = "No activity logged today."

print(f"Status: {status}\n")

# 3. Data Structures Preview
tech_stack = ["Python", "Git", "SQL", "Pandas", "PyTorch"]
user_profile = {
    "role": "AI Student",
    "location": "Poland",
    "target": "Remote AI / Data Analyst Engineer"
}

print(f"Tech Stack to Master: {tech_stack}")
print(f"Career Target: {user_profile['target']}")