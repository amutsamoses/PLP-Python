# This script demonstrates two core concepts in Python:
# 1. File reading and writing (File I/O)
# 2. Exception handling with try-except blocks
#
# Features:
# - Option 1: Reads a sample input file, processes its content
#             (converts to uppercase), and writes to a new file.
# - Option 2: Prompts user for a file name, tries to read it,
#             and handles errors gracefully if it doesn't exist.
# ===============================================================


def file_read_write():
    """
    Reads `sample.txt`, converts its content to uppercase,
    and writes the processed content into `output.txt`.

    Steps:
    1. Open `sample.txt` in read mode.
    2. Read the entire content.
    3. Convert the content to uppercase.
    4. Create or overwrite `output.txt` and write the processed content.
    5. Print a success message or handle errors if the file is missing.
    """
    try:
        # Open and read the content of the input file
        with open("sample.txt", "r") as infile:
            content = infile.read()

        # Process the text by converting it to uppercase
        processed_content = content.upper()

        # Write the processed content to the output file
        with open("output.txt", "w") as outfile:
            outfile.write(processed_content)

        # Notify user of success
        print("✅ Processing complete! Check 'output.txt' for the processed text.\n")

    except FileNotFoundError:
        # Specific error if the input file does not exist
        print("❌ Error: 'sample.txt' was not found. Please create the file first.\n")
    except Exception as e:
        # Generic error handler for any other unexpected errors
        print(f"❌ Unexpected error occurred: {e}\n")


def error_handling_lab():
    """
    Prompts the user to enter a filename, attempts to read it,
    and prints the content if successful. Handles errors if:
    - The file does not exist.
    - Any other unexpected errors occur.
    """
    try:
        # Ask the user for the file they want to read
        filename = input("Enter the filename you want to read: ")

        # Open and read the content of the specified file
        with open(filename, "r") as file:
            content = file.read()

        # Display the file content
        print("\n📂 File Content:\n")
        print(content)

    except FileNotFoundError:
        # Specific error if the entered filename does not exist
        print(f"❌ Error: The file '{filename}' was not found.\n")
    except Exception as e:
        # Generic error handler for other unexpected issues
        print(f"❌ Unexpected error occurred: {e}\n")


# Entry point of the script
if __name__ == "__main__":
    print("=== Week 4: File Handling and Exception Handling ===")
    print("Choose an option:")
    print("1. Process sample.txt and create output.txt")
    print("2. Test error handling by opening a custom file")

    # Prompt user for choice
    choice = input("\nEnter 1 or 2: ")

    # Execute the selected option
    if choice == "1":
        file_read_write()
    elif choice == "2":
        error_handling_lab()
    else:
        # Handle invalid input gracefully
        print("❌ Invalid option. Please run the program again and choose 1 or 2.\n")