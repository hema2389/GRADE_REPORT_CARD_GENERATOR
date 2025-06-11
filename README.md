# 🏫 Student Grade System with Report Card Export

A Python program that collects student marks for multiple subjects, assigns grades, and exports the final report card to both `.txt` and `.xlsx` files — with each subject stored in a **separate Excel sheet**!

---

## 📌 Features

- Accepts dynamic input: any number of students and subjects
- Assigns grades based on predefined mark ranges
- Stores results in a nested dictionary
- Displays a neat report card in the terminal
- Exports:
  - 📄 `report_card.txt`: human-readable format
  - 📊 `report_card_by_subject.xlsx`: separate sheet for each subject

---

## 🎓 Grading Criteria

| Marks Range | Grade  |
|-------------|--------|
| 90–100      | Grade O |
| 80–89       | Grade A |
| 70–79       | Grade B |
| 60–69       | Grade C |
| 50–59       | Grade D |
| 40–49       | Grade E |
| < 40        | Grade F |

---

## 💡 Sample Input & Output

Enter the number of students: 2
Enter the number of subjects: 2
Enter the name of subject 1: Science
Enter the name of subject 2: Maths

Enter name of student 1: Malar
Enter marks in Science: 67
Enter marks in Maths: 88

Enter name of student 2: Nivin
Enter marks in Science: 30
Enter marks in Maths: 45

 Report Card:

 Malar's Performance:
Science: 67.0 → Grade C
Maths: 88.0 → Grade A

 Nivin's Performance:
Science: 30.0 → Grade F
Maths: 45.0 → Grade E

Report card saved as report_card_by_subject.xlsx


---

## 📦 How to Run

1. Make sure you have Python installed.
2. Install required libraries:

```bash
pip install pandas openpyxl

Save your Python file as grade_system.py and run:
python grade_system.py

grade_system/
├── grade_system.py
├── report_card_by_subject.xlsx
└── README.md

✅ Author
Made as part of a Python mini-project learning journey.
