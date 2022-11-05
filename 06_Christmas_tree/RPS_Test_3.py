options = ['paper', 'scissors', 'rock']
user_choice_is_correct = False

while user_choice_is_correct is False:
    user_choice = input(f'What is Your choice ->')
    if user_choice in options:
        user_choice_is_correct = True
    print(user_choice)

# Both do same thing.

user_choice_is_correct = True

while user_choice_is_correct:
    user_choice = input(f'What is Your choice ->')
    if user_choice in options:
        user_choice_is_correct = False
    print(user_choice)