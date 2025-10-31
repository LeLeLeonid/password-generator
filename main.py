import string
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGenerator(tk.Tk):
    """
    A simple password generator application with a GUI.
    """
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("350x200")
        self.resizable(False, True)
        self._center_window()

        # --- UI Elements ---
        self.label = tk.Label(self, text="Enter desired password length:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self, width=30, justify="center")
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.generate_password())

        self.generate_btn = tk.Button(self, text="Generate", command=self.generate_password)
        self.generate_btn.pack(pady=10)

        self.copy_btn = tk.Button(self, text="Copy", command=self.copy_to_clipboard, state=tk.DISABLED)
        self.copy_btn.pack(pady=5)

        # --- Checkboxes ---
        checkbox_frame = tk.Frame(self)
        checkbox_frame.pack(pady=5)

        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        self.dark_theme_enabled = tk.BooleanVar(value=False)

        self.digits_check = tk.Checkbutton(checkbox_frame, text="Digits", variable=self.include_digits, relief="raised")
        self.digits_check.grid(row=0, column=0, padx=5)

        self.symbols_check = tk.Checkbutton(checkbox_frame, text="Symbols", variable=self.include_symbols, relief="raised")
        self.symbols_check.grid(row=0, column=1, padx=5)
        
        self.dark_theme_check = tk.Checkbutton(checkbox_frame, text="Dark Theme", variable=self.dark_theme_enabled, command=self.toggle_dark_theme, relief="raised")
        self.dark_theme_check.grid(row=0, column=2, padx=5)

    def _center_window(self):
        """Centers the window on the screen."""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")

    def generate_password(self):
        """Generates a password based on user-defined criteria."""
        try:
            length = int(self.entry.get())
            if length <= 0:
                length = abs(length)
        except ValueError:
            length = len(self.entry.get())

        chars = string.ascii_letters
        if self.include_digits.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation

        password = "".join(random.choice(chars) for _ in range(length))

        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)
        self.copy_btn.config(state=tk.NORMAL)

    def copy_to_clipboard(self):
        """Copies the generated password to the clipboard."""
        pyperclip.copy(self.entry.get())
        messagebox.showinfo("Success", "Password copied to clipboard!")

    def toggle_dark_theme(self):
        """Toggles the dark theme for the application."""
        if self.dark_theme_enabled.get():
            bg_color = "#2e2e2e"
            fg_color = "white"
            self.configure(bg=bg_color)
            for widget in self.winfo_children():
                if isinstance(widget, tk.Checkbutton):
                    widget.configure(
                        bg=bg_color,
                        fg=fg_color,
                        activebackground=bg_color,
                        activeforeground=fg_color,
                        selectcolor=bg_color,
                        highlightbackground=bg_color,
                        highlightcolor=bg_color
                    )
                elif isinstance(widget, tk.Label):
                    widget.configure(bg=bg_color, fg=fg_color)
                elif isinstance(widget, tk.Button):
                    widget.configure(bg="#4d4d4d", fg=fg_color)
                elif isinstance(widget, tk.Entry):
                    widget.configure(bg="#4d4d4d", fg=fg_color, insertbackground=fg_color)
                elif isinstance(widget, tk.Frame):
                    widget.configure(bg=bg_color)
        else:
            bg_color = "SystemButtonFace"
            fg_color = "black"
            self.configure(bg=bg_color)
            for widget in self.winfo_children():
                if isinstance(widget, tk.Checkbutton):
                    widget.configure(
                        bg=bg_color,
                        fg=fg_color,
                        activebackground=bg_color,
                        activeforeground=fg_color,
                        selectcolor=bg_color,
                        highlightbackground=bg_color,
                        highlightcolor=bg_color
                    )
                elif isinstance(widget, tk.Label):
                    widget.configure(bg=bg_color, fg=fg_color)
                elif isinstance(widget, tk.Button):
                    widget.configure(bg=bg_color, fg=fg_color)
                elif isinstance(widget, tk.Entry):
                    widget.configure(bg="white", fg=fg_color, insertbackground=fg_color)
                elif isinstance(widget, tk.Frame):
                    widget.configure(bg=bg_color)

if __name__ == "__main__":
    app = PasswordGenerator()
    try:
        app.iconbitmap("passgen.ico")
    except tk.TclError:
        # Icon not found, continue without it
        pass
    app.mainloop()
