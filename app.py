import tkinter as tk
from tkinter import filedialog, messagebox
import os

from ocr import handle_file   # your existing OCR logic


def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[
            ("Supported files", "*.png *.jpg *.jpeg *.bmp *.pdf"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        selected_file.set(file_path)


def process_file():
    file_path = selected_file.get()

    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    try:
        text = handle_file(file_path)

        if not text.strip():
            text = "[No text detected]"

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, text)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_output():
    text = output_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Error", "Nothing to save!")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text file", "*.txt")]
    )

    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(text)

        messagebox.showinfo("Success", "File saved!")


# ===== GUI SETUP =====
root = tk.Tk()
root.title("OCR Tool")
root.geometry("700x500")

selected_file = tk.StringVar()

# Title
tk.Label(root, text="OCR File Processor", font=("Arial", 16)).pack(pady=10)

# File path display
tk.Entry(root, textvariable=selected_file, width=80).pack(pady=5)

# Buttons
tk.Button(root, text="Upload File", command=upload_file).pack(pady=5)
tk.Button(root, text="Process", command=process_file).pack(pady=5)

# Output box
output_box = tk.Text(root, wrap="word")
output_box.pack(expand=True, fill="both", padx=10, pady=10)

# Save button
tk.Button(root, text="Save Output", command=save_output).pack(pady=5)

# Run app
root.mainloop() 