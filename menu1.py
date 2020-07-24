from tkinter import *

def ok(event,a,b):
   print(variable.get())

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

variable.trace('w',ok)

mainloop()
