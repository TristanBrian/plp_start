#Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.

def main():
    # Create a tuple of favourite books
    favorite_books = (
        "Rich Dad Poor Dad",
        "Harry potter",
        "Think and Grow Rich",
        "The Millionaire Next door",
        "Child of the Dream"
    )

    print("Favorite books made for Tristan:")
    for book in favorite_books:
        print(book)
if __name__ == "__main__":
        main()
