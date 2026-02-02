correct_answers = ["A", "B", "C", "D", "A"]


def validate_answers():
    student_answers = []
    print("\nEnter your answers:")

    for i in range(len(correct_answers)):
        ans = input(f"Question {i+1} (A/B/C/D): ").upper()
        student_answers.append(ans)

    return student_answers

def calculate_score(student_answers):
    score = 0

    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            score += 1

    return score

def generate_grade(score):
    if score == 5:
        return "A"
    elif score >= 3:
        return "B"
    elif score == 2:
        return "C"
    else:
        return "Fail"

def main():
    answers = validate_answers()
    score = calculate_score(answers)
    grade = generate_grade(score)

    print("\n--- Exam Result ---")
    print("Total Questions:", len(correct_answers))
    print("Score:", score)
    print("Grade:", grade)

main()
