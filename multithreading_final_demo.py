import tkinter as tk
import threading
import queue
import time

class Newthread(threading.Thread):
    def __init__(self, n, q):
        threading.Thread.__init__(self)
        self.n = n
        self.q = q

    def run(self):
        i = 0
        while i <= self.n:
            self.q.put(i)
            i += 1
            time.sleep(1)
        return



def update_progress(t):
    if not t.is_alive() and t.q.empty():
        return
    y = 0
    while not t.q.empty():
        x = t.q.get()
        y = int((x/t.n) * 100)
    if y!=0:
        label.configure(text = str((y)) + '%')
    label.after(1000, lambda : update_progress(t))
    return
        
def start_process(n:int) -> None:
    q = queue.Queue()
    t = Newthread(n, q)
    t.start()
    update_progress(t) #checks the work done and updates the progress bar accordingly
    


if __name__ == '__main__':
    app = tk.Tk()
    frame = tk.Frame(app)
    frame.grid(row = 0, column = 0,rowspan = 1, columnspan = 1, sticky = 'nsew')

    label = tk.Label(frame, text = '0%')
    label.pack()

    start_process(60)
    app.mainloop()
