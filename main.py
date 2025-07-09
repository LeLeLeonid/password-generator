import string as s
import random as r
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator v.1 (by LeLeLeonid)")
        self.geometry("300x150+500+500")
        self.resizable(True, True)
        
        self.label = tk.Label(self, text="Choose your length!")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=5)
        self.entry.bind(("<Return>"), self.on_enter)

        self.btn = tk.Button(self, text="Generate", command=self.generate)
        self.btn.pack(pady=10)
        
    def on_enter(self, event):
        self.generate()

    def generate(self):
        letters = s.ascii_letters
        digits = s.digits
        symbols = s.punctuation
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
    
        self.label.config(text=f"Your Generated Password's Length: {length}")
    
        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)

if __name__ == "__main__":
    app = Main()
    app.iconbitmap("passgen.ico")
    app.mainloop()
