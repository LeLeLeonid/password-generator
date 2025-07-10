import string as s
import random as r
import tkinter as tk
import pyperclip as pc

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Password Generator v.1.1 (by LeLeLeonid)")
        self.update_idletasks()
        
        # Gets window sizes
        
        #width = self.winfo_width()
        #height = self.winfo_height()
        
        x = (self.winfo_screenwidth() // 2) - (300 // 2)
        y = (self.winfo_screenheight() // 2) - (150 // 2)
        
        self.geometry(f"300x150+{x}+{y}")
        self.resizable(True, False)
        
        self.label = tk.Label(self, text="Choose your length!")
        self.label.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

        self.entry = tk.Entry(self, width=30, justify="center")
        self.entry.grid(row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        self.entry.bind(("<Return>"), self.on_enter)

        self.btn_quit = tk.Button(self, text="Quit", command=self.destroy)
        self.btn_quit.grid(row=2, column=0, padx=5, pady=10)
        
        self.btn = tk.Button(self, text="Generate", width=10, height=2, command=self.generate)
        self.btn.grid(row=2, column=1, padx=5, pady=10)

        self.btn_copy = tk.Button(self, text="Copy", command=self.copy)
        self.btn_copy.grid(row=2, column=2, padx=5, pady=10)
        self.btn_copy.config(state=tk.DISABLED)

        self.var1 = tk.BooleanVar(value=True)
        self.var2 = tk.BooleanVar(value=True)
        self.chk1 = tk.Checkbutton(self, text="Digits", variable=self.var1, command=self.check_state)
        self.chk2 = tk.Checkbutton(self, text="Symbols", variable=self.var2, command=self.check_state)
        self.chk1.grid(row=3, column=0, padx=5)
        self.chk2.grid(row=3, column=1, padx=5)

        self.dark_var = tk.BooleanVar(value=False)
        self.dark_chk = tk.Checkbutton(self, text="Dark Theme (Alpha)", variable=self.dark_var, command=self.check_state)
        self.dark_chk.grid(row=3, column=2, padx=5)

        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

    def copy(self):
        password = self.entry.get()
        pc.copy(password)
        
    def on_enter(self, event):
        self.generate()

    def check_state(self):
        if self.dark_var.get():
            self.configure(bg="black")
            self.label.configure(bg="black", fg="white")
            self.btn.configure(bg="black", fg="white")
        else:
            self.configure(bg="white")
            self.label.configure(bg="white", fg="black")
            self.btn.configure(bg="white", fg="black")
            
    def generate(self):
        letters = s.ascii_letters
        digits = s.digits if self.var1.get() else ""
        symbols = s.punctuation if self.var2.get() else ""
        chars = letters + digits + symbols
    
        try:
            length = int(self.entry.get())
            if length <= 0:
                raise ValueError("Length must be positive *o*")
        except Exception as e:
            text = self.entry.get()
            length = len(text)
            if length == 0:
                length = r.randint(6, 12)
    
        password = "".join(r.choice(chars) for _ in range(length))
    
        self.label.config(text=f"Your Generated Password Length: {length}")
    
        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)
        self.btn_copy.config(state=tk.NORMAL)

if __name__ == "__main__":
    app = Main()
    app.iconbitmap("passgen.ico")
    app.mainloop()
