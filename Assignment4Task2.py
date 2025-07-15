def modify_file(filename="output.txt"):

    try:
        # Get user input and write to file (overwrite if exists)
        with open(filename, "w") as f:
            user_input = input("Enter text to write to the file: ")
            f.write(user_input + "\n")

        # Append more data to the file
        with open(filename, "a") as f:
            more_input = input("Enter additional text append: ")
            f.write(more_input + "\n")

        # Read and display the file content
        with open(filename, "r") as f:
            content = f.read()
            print("\nFinal content of the file:")
            print(content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    modify_file()