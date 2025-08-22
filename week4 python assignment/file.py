# File Read & Write Challenge
try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify content (example: uppercase)
    modified = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified)

    print(" File has been read and modified content written to output.txt")

except FileNotFoundError:
    print(" input.txt not found. Please create the file first.")
