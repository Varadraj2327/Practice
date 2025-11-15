
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest egg?: ",
             "What is the most abundant gas in nature?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 119 ", "B. 101 ", "C. 118 ", "D. 116 "), 
           ("A. Whale ", "B. Dodo ", "C. Elephant ", "D. Ostrich "), 
           ("A. Oxygen ", "B. Carbon ", "C. Nitrogen ", "D. Sodium "), 
           ("A. 206 ", "B. 207 ", "C. 232 ", "D. 200 "), 
           ("A. Earth ", "B. Mars ", "C. Venus ", "D. Saturn "))

answers = ("C", "D", "C", "A", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")