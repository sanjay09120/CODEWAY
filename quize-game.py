questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "G", "Go"],
        "answer": "Au"
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Jupiter", "Venus", "Mars", "Saturn"],
        "answer": "Mars"
    }
]
def load_questions():
    return questions

def display_question(question):
    print(question["question"])
    for idx, option in enumerate(question["options"], 1):
        print(f"{idx}. {option}")
    user_answer = int(input("Please enter the number of your answer: "))
    return user_answer

def evaluate_answer(user_answer, correct_option_index):
    return user_answer == correct_option_index

def play_quiz():
    score = 0
    questions = load_questions()
    
    for question in questions:
        correct_option_index = question["options"].index(question["answer"]) + 1
        user_answer = display_question(question)
        
        if evaluate_answer(user_answer, correct_option_index):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")
    
    print(f"Your final score is: {score}/{len(questions)}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_quiz()
    else:
        print("Thank you for playing!")

play_quiz()
