# enter input and use conditional statements

marks = int(input("Enter the number: "))

if marks < 0 or marks >100:
    print("Invalid Number.Enter a number between 1 and 100")

elif marks >= 90: 
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks <= 50:
    print("Grade E")
else:
    print("Fail")

# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). 
# The else clause is optional.