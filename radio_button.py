import tkinter as tk

def sel():
    label.configure(text = 'You have selected :' +  str(var.get()))
    return

if __name__ == '__main__':
    root = tk.Tk()

    label = tk.Label(root)
    label.pack()

    l = []
    
    var = tk.IntVar()
    l.append(var)
    r1 = tk.Radiobutton(root, text = 'Option1', variable = var, value = 1, command = sel)
    r1.pack()

    l.append(var)
    r2 = tk.Radiobutton(root, text = 'Option2', variable = var, value = 2, command = sel)
    r2.pack()
    
    
