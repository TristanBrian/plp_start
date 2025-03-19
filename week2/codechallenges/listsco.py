#Create a program that stores a list of words.
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

def main():
    # Initialize an empty list to store words
    words = []

    # Ask the user how many words they want to enter
    num_words = int(input("How many words do you want to enter? "))

    # Loop to accept user input for the words
    for i in range(num_words):
        word = input(f"Enter word {i + 1}: ")
        words.append(word)

    # Use list comprehension to filter words with an odd number of characters
    odd_length_words = [word for word in words if len(word) % 2 != 0]

    
# Use list comprehension to filter words with an even number of characters
    even_length_words = [word for word in words if len(word) % 2 == 0]


    # Print the original list and the filtered list
    print("\nOriginal list of words:", words)
    print("Words with an odd number of characters:", odd_length_words)
    print("Words with an even number of characters:", even_length_words)
    
if __name__ == "__main__":
    main()