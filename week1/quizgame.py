def quiz():
    import os

    # Define the quiz questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
            "answer": "B"
        },
        {
            "question": "Which of the following is NOT a Python data type?",
            "options": ["A. int", "B. float", "C. string", "D. double"],
            "answer": "D"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "options": ["A. Steven Spielberg", "B. Christopher Nolan", "C. Quentin Tarantino", "D. James Cameron"],
            "answer": "B"
        },
        {
            "question": "What is the result of 2 ** 3 in Python?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 16"],
            "answer": "B"
        },
        {
            "question": "Which movie features a character named 'Forrest Gump'?",
            "options": ["A. The Shawshank Redemption", "B. Forrest Gump", "C. The Godfather", "D. Pulp Fiction"],
            "answer": "B"
        }
    ]

    # Clear the terminal screen for a clean start
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Quiz Game! 🎉\n")
    print("You will be asked a series of multiple-choice questions. Enter the letter (A, B, C, or D) of your answer.\n")
    input("Press Enter to start the quiz...")
    os.system('cls' if os.name == 'nt' else 'clear')

    score = 0

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        # Validate user input
        while True:
            user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")

        # Check if the answer is correct
        if user_answer == q['answer']:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}. 😢\n")

        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display final score
    print(f"Quiz ended! Your final score is {score}/{len(questions)}! 🏆\n")

    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ["yes", "no"]:
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    if play_again == "yes":
        quiz()
    else:
        print("Thanks for playing! Tristan says hi! 👋")

# Start the quiz
quiz()