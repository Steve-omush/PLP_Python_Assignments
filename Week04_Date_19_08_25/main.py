"""
File Read & Write Challenge 🖋️
This program:
1. Asks the user for a filename to read.
2. Reads the file content (if it exists).
3. Modifies the content (uppercase example).
4. Writes the modified content to a new file.
5. Handles errors gracefully.
"""

def process_file():

    try:
        # Ask the user for a filename
        filename = input("Enter the name of file to read: ")

        # Try to open the file for reading
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Modify the content (make it uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.write(modified_content)

        print(f"File '{filename}' read successfully.")
        print(f"Modified file saved as '{new_filename}'.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program completed.")

if __name__ == "__main__":
    process_file()
