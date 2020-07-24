import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk as ttk
import random as R
import timeit
import threading
import queue

class Work(threading.Thread):
    def __init__(self, n, q, a, b, numbers:list):
        threading.Thread.__init__(self)
        self.n = n;
        self.q = q
        self.a = a
        self.b = b
        self.numbers = numbers

    def run(self):
        for i in range(self.n):
            self.q.put(i)
            self.numbers.append(str(R.randint(self.a, self.b)))
        

def inside():
    print(R.randint(1, 10000000))

def update_progress(w, q):
    if not w.is_alive() and q.empty():
        return
    x = -1
    while not q.empty():
        x = q.get() + 1 
    if x!=-1:
        progress_bar['value'] = x
        print(x)
        if x == w.n:
            completed.configure(text = 'Successfully generated!!')
    progress_bar.after(100, lambda : update_progress(w, q))
    return
    

def generate_numbers(n, min_value, max_value, delimiter:chr, results):
    erase_info()
    try:
        n, a, b = int(n.get()), int(min_value.get()), int(max_value.get())
        assert a<=b
        error_label.configure(text = '')

        progress_bar.grid(row = 6, column = 0, rowspan = 1, columnspan = 4, sticky = 'we')
        progress_bar['maximum'] = n
    except AssertionError:
        error_label.configure(text = 'Min Value must be less than Max Value')
        return
    except:
        print('something wrong')
        #print('First Three fields must contain integers only!')
        error_label.configure(text = 'First three fields must contain integers only!!!')
        return

    ch = delimiter
    #print(ch)
    if ch == '' : ch = ','
    numbers = []

    q = queue.Queue()
    w = Work(n, q, a, b, numbers)
    w.start()
    progress_bar.after(100, lambda : update_progress(w, q))
    
    '''    
    for i in range(n):
        progress_bar['value'] = i+1
        #print(i+1)
        #numbers.append(str(R.randint(a, b)))
    '''
    results.append(ch.join(numbers))
    #print('completed')

    save['state'] = 'normal'
    
    return

def erase_info():
    progress_bar.grid_forget()
    error_label.configure(text = '')
    completed.configure(text = '')
    return

def reset_fields(*args):
    for a in args:
        a.delete(0, tk.END)
        a.insert(0, '')
    erase_info()
    return

def get_filename():

    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')]
    

    file = fd.asksaveasfile(filetypes = files, defaultextension = '.txt')
    return file

def save_results(results:list):
    print(results)
    results = results[0]
    file = get_filename()
    if file == None:
        return
    file.write(results)
    file.close()
    return
        
if __name__ == '__main__':

    
    app = tk.Tk()
    app.title('Generate Random Numbers')
    W, H = 500, 500
    app.geometry(str(W) + 'x' + str(H))
    app.resizable(False, False)

    #preparing menu

    menu_frame = ttk.Frame(app)
    menu_frame.place(relheight = 0.1, relwidth = 1)

    menu_bar = tk.Menu(app)

    file = tk.Menu(menu_bar, tearoff = 0)
    file.add_command(label = 'First file', command = inside)
    file.add_command(label = 'Second file', command = inside)
    file.add_command(label = 'Third file', command = inside)

    edit = tk.Menu(menu_bar, tearoff = 0)
    edit.add_command(label = 'First edit', command = inside)
    edit.add_command(label = 'Second edit', command = inside)
    edit.add_command(label = 'Third edit', command = inside)

    about = tk.Menu(menu_bar, tearoff = 0)
    about.add_command(label = 'First Label', command = inside)
    about.add_command(label = 'Second Label', command = inside)

    menu_bar.add_cascade(label = 'File', menu = file)
    menu_bar.add_cascade(label = 'Edit', menu  = edit)
    menu_bar.add_cascade(label = 'About', menu = about)

    app.configure(menu = menu_bar)
    #menu prepared

    frame = ttk.Frame(app)
    frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.6)

    f = ('Arial', 12)

    #Number of Values : {number}
    label = ttk.Label(frame, text = 'Number of Values : ', font = f)
    label.grid(row = 0, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    n = ttk.Entry(frame, font = f)
    n.grid(row = 0, column = 2, rowspan = 1, columnspan = 2, padx = 10,  pady = 10)

    #Minimum Value : {number}
    label = ttk.Label(frame, text = 'Minimum Value : ', font = f)
    label.grid(row = 1, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    min_value = ttk.Entry(frame, font = f)
    min_value.grid(row = 1, column = 2, rowspan = 1, columnspan = 2, padx = 10, pady = 10)

    #Maximum Value : {number}
    label = ttk.Label(frame, text = 'Maximum Value : ', font = f)
    label.grid(row = 2, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    max_value = ttk.Entry(frame, font = f)
    max_value.grid(row = 2, column = 2, rowspan = 1, columnspan = 2, padx = 10, pady = 10)

    #Delimiter (Optional, default = ',')
    variable = tk.StringVar()
    OPTIONS = {
        'Comma' : ',',
        'New Line' : '\n',
        'Space' : ' ',
        'Dot' : '.',
        }
    label = ttk.Label(frame, text = 'Delimiter : ', font = f)
    label.grid(row = 3, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    options = ttk.OptionMenu(frame, variable, *(['Comma'] + list(OPTIONS.keys())))
    options.grid(row = 3, column = 2, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    #delimiter = tk.Entry(frame, font = f)
    #delimiter.grid(row = 3, column = 2, rowspan = 1, columnspan = 2, padx = 10, pady = 10)

    error_label = tk.Label(frame, font = f, fg = 'red', bd = 5)
    error_label.grid(row = 4, column = 0, rowspan = 1, columnspan = 4, padx = 10, pady = 20, sticky = 'we')

    #completed task notification
    completed = tk.Label(frame, font = f, fg = 'green', bd = 5)
    completed.grid(row = 5, column = 0, rowspan = 1, columnspan = 4, padx = 10, sticky = 'we')

    #progress_bar.grid(row = 5, column = 0, rowspan = 1, columnspan = 4, padx = 10, sticky = 'we')
    progress_bar = ttk.Progressbar(frame)


    

    #buttons frame
    frame2 = ttk.Frame(app)
    frame2.place(relx = 0.1, rely = 0.7, relwidth = 0.8, relheight = 0.2)

    #generate numbers
    results = []
    gen = ttk.Button(frame2, text = 'Generate!', command = (lambda : generate_numbers(n, min_value, max_value, OPTIONS[variable.get()],results)))
    gen.pack(anchor = 'w', side = tk.LEFT, padx = 10, pady = 20)

    #reset fields
    reset = ttk.Button(frame2, text = 'Reset All Fields', command = (lambda : reset_fields(n, min_value, max_value)))
    reset.pack(anchor = 'w', side = tk.LEFT, padx = 10, pady = 20)

    #save results
    save = ttk.Button(frame2, text = 'Save Result', command = (lambda : save_results(results)))
    save.pack(anchor = 'w', side = tk.LEFT, padx = 10, pady = 20)
    save['state'] = 'disabled'
    
    
    
    
    
    app.mainloop()


'''
    #Filename : {string}
    label = tk.Label(frame, text = 'Save as file : ', font = f)
    label.grid(row = 4, column = 0, rowspan = 1, columnspan = 2, padx = 10, pady = 10, sticky = 'w')
    filebutton = tk.Button(frame, text = 'Open', font = f, command = get_filename)
    filebutton.grid(row = 4, column = 2, rowspan = 1, columnspan = 1, padx = 10, pady = 10)
'''
