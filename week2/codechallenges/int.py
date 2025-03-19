#Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

def main():
    # Initialize an empty list
    integer_list = []

    # Enter number of integers you want in the list
    num_integers = int(input("How many integers do you want to include in the list? "))

    # Loop to accept user input for the list of integers
    for i in range(num_integers):
        while True:
            try:
                # Prompt user to enter an integer
                integer = int(input(f"Enter integer {i + 1}: "))
                # Add integer to list
                integer_list.append(integer)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    # Compute the sum of all integers in the list
    total_sum = sum(integer_list)

    # Display the list and the sum
    print(f"The list of integers is: {integer_list}")
    print(f"The sum of all integers in the list is: {total_sum}")

if __name__ == "__main__":
    main()