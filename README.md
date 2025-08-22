# 📘 File Handling & Error Handling in Python

This project contains a single exercise divided into two parts:  

1. **File Read & Write Challenge**  
2. **Error Handling Lab**  

Both are focused on practicing **file handling** and **exception management** in Python.  

---

## 🖋️ File Read & Write Challenge  

In this part, the program:  
- Opens an existing file named **`input.txt`** in **read mode**.  
- Reads its entire content.  
- **Modifies the content** by converting it to **uppercase**.  
- Creates and writes the modified content into a new file called **`output.txt`**.  
- Prints a confirmation message if successful.  

If the file `input.txt` does not exist, the program handles it by showing:  
```
❌ input.txt not found. Please create the file first.
```

---

## 🧪 Error Handling Lab  

In this part, the program:  
- Asks the user to **type the name of a file**.  
- Attempts to open and read the file.  
- Prints its contents on the screen if found.  
- If the file does **not exist**, it catches the `FileNotFoundError` and shows an error message.  
- If the file exists but cannot be accessed, it catches a `PermissionError`.  
- For any other issue, it shows a generic error message.  

Example successful run:  
```
Enter the filename to read: notes.txt
📂 File contents:

This is a test file.
```

Example error run:  
```
Enter the filename to read: missing.txt
❌ The file 'missing.txt' does not exist.
```

---

## 🛠️ How to Run  

1. Save the code into a Python file (e.g., `file_tasks.py`).  
2. Ensure Python 3 is installed.  
3. Run the program from a terminal or command prompt:  
   ```bash
   python file_tasks.py
   ```  

---

## 🎯 Learning Outcomes  

From these two programs, you practice:  
- **Opening and reading files** with `open()`  
- **Writing data to new files**  
- **Basic content modification** (changing text to uppercase)  
- **Error handling** using `try-except` for:  
  - `FileNotFoundError`  
  - `PermissionError`  
  - Other generic exceptions  
