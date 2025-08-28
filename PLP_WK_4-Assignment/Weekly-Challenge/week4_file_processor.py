# Program to read a text file, process its content, and write results to a new file.

def process_file(input_file, output_file):
    """
    Reads content from input_file, converts text to uppercase,
    counts total words, and writes the processed content and
    word count into output_file.
    
    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    try:
        # Read content from input file
        with open(input_file, "r") as infile:
            content = infile.read()

        # Count the words
        words = content.split()
        word_count = len(words)

        # Convert text to uppercase
        processed_content = content.upper()

        # Write processed content and word count to output file
        with open(output_file, "w") as outfile:
            outfile.write(processed_content)
            outfile.write(f"\n\nWORD COUNT: {word_count}\n")

        # Print success message
        print(f"Success! Processed text has been saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Please create the file and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("--- Week 4 File Processing Challenge ---")
    process_file("input.txt", "output.txt")