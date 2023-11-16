import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class PythonToExeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Python to EXE Converter")
        root.resizable(0,0)
        # Create widgets
        self.label_file = tk.Label(root, text="Select a Python file:")
        self.label_file.pack(pady=10)

        self.browse_file_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_file_button.pack(pady=10)

        self.label_icon = tk.Label(root, text="Select an icon file (optional):")
        self.label_icon.pack(pady=10)

        self.browse_icon_button = tk.Button(root, text="Browse", command=self.browse_icon)
        self.browse_icon_button.pack(pady=10)

        self.label_status = tk.Label(root, text="")
        self.label_status.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert to EXE", command=self.convert_to_exe)
        self.convert_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.python_file_path = file_path
            self.label_file.config(text=f"Selected Python file: {os.path.basename(file_path)}")

    def browse_icon(self):
        icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if icon_path:
            self.icon_path = icon_path
            self.label_icon.config(text=f"Selected icon file: {os.path.basename(icon_path)}")

    def convert_to_exe(self):
        if hasattr(self, 'python_file_path'):
            output_directory = filedialog.askdirectory()
            if output_directory:
                output_path = os.path.join(output_directory, "output.exe")

                # Add the --icon option if an icon file is selected
                icon_option = f"--icon={self.icon_path}" if hasattr(self, 'icon_path') else ""

                command = ["pyinstaller", "--onefile", "--noconsole", icon_option, self.python_file_path, "--distpath", output_directory]
                subprocess.run(command)

                messagebox.showinfo("Conversion Complete", f"The EXE file is saved at:\n{output_path}")
            else:
                messagebox.showwarning("Output Directory Not Selected", "Please select an output directory.")
        else:
            messagebox.showwarning("Python File Not Selected", "Please select a Python file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonToExeConverter(root)
    root.mainloop()
