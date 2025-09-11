from idlelib.rpc import response_queue


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0  # use index instead of 1-based

    for key in questions:
        print("---------------")
        print(key)

        # print the multiple choice options
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        # map A/B/C/D to actual answers
        answer_index = ["A", "B", "C", "D"].index(guess)
        user_answer = options[question_num][answer_index]

        correct_guesses += check_answer(questions[key], user_answer)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------")
    print("Results")
    print("---------------------")

    print("Answers: ", end="")
    for i in questions.values():
        print(i, end=" | ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" | ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():

    response = input("Play again?: (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "What is the capital of France?": "Paris",
    "Which data type is used to store True/False values in Python?": "bool",
    "What keyword is used to define a function in Python?": "def",
    "What does the 'len()' function do?": "Returns the length of an object",
    "What symbol is used for comments in Python?": "#"
}

options = [
    ["Berlin", "Madrid", "Paris", "Rome"],
    ["int", "str", "bool", "list"],
    ["def", "func", "lambda", "define"],
    ["Adds numbers", "Returns the length of an object", "Creates a list", "Converts to string"],
    ["//", "#", "/* */", "--"]
]

new_game()

while play_again():
    new_game()

print("Bye Bye")
