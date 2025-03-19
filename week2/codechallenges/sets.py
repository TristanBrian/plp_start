#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
def main():
    # Initialize empty sets
    set1 = set()
    set2 = set()

    # Input for set1
    print("Enter the number of elements in set1:")
    n = int(input())
    print("Enter the elements of set1:")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Element {i + 1}: "))
                set1.add(element)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    # Input for set2
    print("Enter the number of elements in set2:")
    n = int(input())
    print("Enter the elements of set2:")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Element {i + 1}: "))
                set2.add(element)
                break
            except ValueError:
                print("Invalid input! Please enter an integer.")

    # Find common elements
    common_elements = set1 & set2

    # Display the result
    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("There are no common elements between the two sets.")

if __name__ == "__main__":
    main()