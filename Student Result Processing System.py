def input_marks():
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)
    return marks


def calculate_total_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


def display_result(total, average, grade):
    print("\n----- Student Result -----")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)


marks = input_marks()
total, average = calculate_total_average(marks)
grade = assign_grade(average)
display_result(total, average, grade)
