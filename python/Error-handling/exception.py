def process_file():
    try:
        # Get filename from user
        input_filename = input("Enter the input filename: ")
        
        # Try to open and read the file
        with open(input_filename, "r") as input_file:
            content = input_file.read()
            
            # Process the content
            word_count = len(content.split())
            processed_content = content.upper()
            
            # Create output filename by adding '_processed' before extension
            output_filename = input_filename.rsplit('.', 1)[0] + '_processed.' + input_filename.rsplit('.', 1)[1]
            
            # Write processed content to new file
            with open(output_filename, "w") as output_file:
                output_file.write(processed_content)
                output_file.write(f"\nWord Count: {word_count}")
                
            print(f"Success! Processed file saved as {output_filename}")
            print(f"Total words: {word_count}")
            
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: No permission to access '{input_filename}'.")
    except IndexError:
        print("Error: Invalid filename format.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    process_file()