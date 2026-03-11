def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter mark: "))
    marks.append(mark)

average = sum(marks) / n
grade = calculate_grade(average)

print("Average:", average)
print("Grade:", grade)
