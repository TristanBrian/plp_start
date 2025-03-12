import random

# List of jokes (Python and programming-themed)
jokes = [
    "Why do Python programmers prefer snakes? Because they love Python! 🐍",
    "Why don't programmers like nature? It has too many bugs. 🐛",
    "Why did the programmer go broke? Because he used up all his cache. 💸",
    "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25! 🎃🎄",
    "Why did the Python data scientist get kicked out of school? Because he couldn't stop importing things! 📚",
    "Why do Python developers never get lost? Because they always follow the snake. 🐍",
    "Why did the programmer quit his job? He didn't get arrays. 😢",
    "Why do programmers hate coffee? Because it turns them into Java developers. ☕",
    "Why did the Python function break up with the other function? It had too many arguments. 💔",
    "Why do programmers prefer dark mode? Because light attracts bugs. 🐜",
    "Why did the programmer get stuck in the shower? He forgot to exit the loop. 🔄",
    "Why do Python programmers wear glasses? Because they can't C#. 👓",
    "Why did the programmer go to therapy? He had too many unresolved issues. 🛠️",
    "Why do programmers always confuse Christmas and Halloween? Because Oct 31 == Dec 25. 🎃🎄",
    "Why did the Python developer go broke? Because he kept raising exceptions. 💸",
]

def display_joke():
    # Clear the terminal for a clean display
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Random Joke Generator! 🤣\n")
    input("Press Enter to get a random joke...")

    # Select a random joke
    joke = random.choice(jokes)
    print(f"\n🎉 Here's your joke:\n\n{joke}\n")

    # Ask if the user wants another joke
    while True:
        another_joke = input("Do you want another joke? (yes/no): ").strip().lower()
        if another_joke in ["yes", "no"]:
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

    if another_joke == "yes":
        display_joke()
    else:
        print("\nThanks for laughing! Goodbye! 👋")

# Start the joke generator
display_joke()