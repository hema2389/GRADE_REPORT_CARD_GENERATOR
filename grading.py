def grade(mark):
    if mark >= 90:
        return 'Grade O'
    elif mark >= 80:
        return 'Grade A'
    elif mark >= 70:
        return 'Grade B'
    elif mark >= 60:
        return 'Grade C'
    elif mark >= 50:
        return 'Grade D'
    elif mark >= 40:
        return 'Grade E'
    else:
        return 'Grade F'

students = {}

n = int(input("Enter the number of students: "))
s = int(input("Enter the number of subjects: "))

subject_names = []
for i in range(s):
    subject = input(f"Enter the name of subject {i+1}: ")
    subject_names.append(subject)

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    students[name] = {}

    for subject in subject_names:
        try:
            mark = float(input(f"Enter marks in {subject}: "))
            grading = grade(mark)
            students[name][subject] = (mark, grading)
        except ValueError:
            print("Invalid marks. Please enter a number.")

#  Print Report Card
print("\n Report Card:")
for student, records in students.items():
    print(f"\n {student}'s Performance:")
    for subject, (mark, g) in records.items():
        print(f"{subject}: {mark} → {g}")
