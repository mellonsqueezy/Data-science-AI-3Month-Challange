# -------------------------------------------------------------
# DAY 3: Python Functions, Modular Code & Metrics
# -------------------------------------------------------------

# 1. Basic Function Definition
def greet_student(name: str, target_role: str = "AI Engineer") -> str:
    """Returns a customized welcome message."""
    return f"Welcome {name}! Target Role: {target_role}."


# 2. Data Processing Function
def process_experiment_results(scores: list[float], threshold: float = 0.70) -> dict:
    """
    Calculates average accuracy score and filters successful ML experiments.
    """
    if not scores:
        return {"error": "Empty score list provided"}

    avg_score = sum(scores) / len(scores)
    successful_experiments = [s for s in scores if s >= threshold]
    
    return {
        "total_experiments": len(scores),
        "average_score": round(avg_score, 4),
        "successful_experiments": successful_experiments,
        "success_rate": f"{(len(successful_experiments) / len(scores)) * 100:.1f}%"
    }


# 3. Execution Block
if __name__ == "__main__":
    # Test Greeting
    print(greet_student("Developer", "AI & Data Science Specialist"))
    print("-" * 50)

    # Test ML Accuracy Scores
    model_accuracies = [0.65, 0.82, 0.91, 0.58, 0.77, 0.88]
    metrics = process_experiment_results(scores=model_accuracies, threshold=0.75)

    print("--- ML Experiment Analysis Results ---")
    for key, value in metrics.items():
        print(f"{key.upper()}: {value}")