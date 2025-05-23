#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary.
#  Then, print the dictionary to the console
def main():
    # Create a dictionary to store person information
    person = {}

    # Prompt user for input
    person["name"] = input("Enter your name: ")

    # Ensure age is a valid integer
    while True:
        try:
            person["age"] = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for age.")

    person["favorite_color"] = input("Enter your favorite color: ")

    # Display the dictionary in a user-friendly format
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")

# Call the main function
if __name__ == "__main__":
    main()