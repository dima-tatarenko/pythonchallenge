import random

names = ["Alex", "Beth", "Caroline", "James", "Ori"]

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

passed = {student for student in student_scores if student_scores[student] > 50}
passed_v2 = {student:score for (student, score) in student_scores.items() if score > 50}
print(passed_v2)

import pandas

# for (index, row) in student_df.iterrows():
#     if row.student == "Angela"