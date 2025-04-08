#  Create a program that reads a file and writes a modified version to a new file. 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
 
import os

def modify_content(content):
    """Example modification: Convert text to uppercase"""
    return content.upper()

def main():
    # Get input filename from user
    filename = input("Enter the filename to read: ")

    # Attempt to read the file
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        return
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return

    # Modify the content
    modified_content = modify_content(content)

    # Create new filename
    base, ext = os.path.splitext(filename)
    new_filename = f"{base}_modified{ext}"

    # Attempt to write the modified content
    try:
        with open(new_filename, 'w') as file:
            file.write(modified_content)
        print(f"Successfully created modified file: {new_filename}")
    except PermissionError:
        print(f"Error: Permission denied to write to '{new_filename}'.")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()