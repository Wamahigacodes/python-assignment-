# Error Handling Lab
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        print(" File contents:\n")
        print(f.read())

except FileNotFoundError:
    print(f" The file '{filename}' does not exist.")
except PermissionError:
    print(f" You don't have permission to read '{filename}'.")
except Exception as e:
    print(f" An error occurred: {e}")
