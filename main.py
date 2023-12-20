import tkinter as tk
from tkinter import filedialog

def extract_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    extracted_lines = [line.split('|')[0].strip() for line in lines]
    with open('extracted_file.txt', 'w') as extracted_file:
        extracted_file.writelines('\n'.join(extracted_lines))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        extract_text(file_path)
        result_label.config(text="Extraction completed. Check extracted_file.txt.")

# Create the main window
root = tk.Tk()
root.title("Text Extraction GUI")

# Create and pack widgets
instructions_label = tk.Label(root, text="Select a text file to extract text:")
instructions_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
