# 5 users ask for 4 school subject, check if they are repeated in the lists.
# Print the most popular subject.
# Remember, user can use capital letters, lowercase or with first capital letter.
print(f'This program search for most popular school subject.')
print(f'It will ask 5 users for 4 most popular subjects...')
user_count = 0
school_subjects = {}
while user_count < 2:
    user_count += 1
    user_name = input(f'What is your name -> ')
    subject_count = 0
    subjects = []
    while subject_count < 2:
        subject_count += 1
        subject = input(f'What was Your favorite school subject {subject_count} -> ')
        subjects.append(subject.title())
    school_subjects[user_name.title()] = subjects
subjects_sum = []
for key in school_subjects:
    subjects_sum += school_subjects[key]
most_popular = {}
for subject in subjects_sum:
    most_popular[subject] = subjects_sum.count(subject)
for key, val in most_popular:

