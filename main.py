import secrets,string,sys
try:import tkinter as tk
except:tk=None
L=string.ascii_letters
D=string.digits
S=string.punctuation
def pwd(n,d,s):
    c=L+(D if d else"")+(S if s else"")
    return"".join(secrets.choice(c)for _ in range(n))
def cli(a):
    n=16
    d=True
    s=True
    if"--help"in a or"-h"in a:
        print("usage: python main.py [length] [--no-digits] [--no-symbols]")
        return
    for x in a:
        if x=="--no-digits":d=False
        elif x=="--no-symbols":s=False
        elif x.isdigit():n=max(1,min(1024,int(x)))
    print(pwd(n,d,s))
def gen(_=None):
    try:n=max(1,min(1024,int(e.get())))
    except Exception:n=16
    o.set(pwd(n,d.get(),s.get()))
def cpy():
    try:
        r.clipboard_clear()
        r.clipboard_append(o.get())
        r.update()
        b.configure(text="Copied!")
        r.after(1200,lambda:b.configure(text="Copy"))
    except Exception:pass
if __name__=="__main__":
    if len(sys.argv)>1 or tk is None:cli(sys.argv[1:])
    else:
        try:
            r=tk.Tk()
            r.title("Password Generator")
            r.minsize(260,220)
            d=tk.BooleanVar(value=True)
            s=tk.BooleanVar(value=True)
            o=tk.StringVar()
            e=tk.Entry(r,justify="center")
            e.insert(0,"16")
            e.pack(fill="x",padx=12,pady=(12,4))
            tk.Checkbutton(r,text="Digits",variable=d).pack()
            tk.Checkbutton(r,text="Symbols",variable=s).pack()
            tk.Entry(r,textvariable=o,justify="center",state="readonly").pack(fill="x",padx=12,pady=8)
            tk.Button(r,text="Generate",command=gen).pack(fill="x",padx=12,pady=2)
            b=tk.Button(r,text="Copy",command=cpy)
            b.pack(fill="x",padx=12,pady=2)
            r.bind("<Return>",gen)
            gen()
            r.mainloop()
        except Exception:cli([])
