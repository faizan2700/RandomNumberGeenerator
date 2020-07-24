import tkinter as tk
import queue
import threading
import time

class Mythread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.counter = 0

    def run(self):
        while True:
            self.counter += 1
            time.sleep(1)
            self.queue.put(1)
            if self.counter == 100:
                break

class Process(object):
    def __init__(self, n, frame):
        self.n = n
        self._queue = queue.Queue()
        self.bar = 0
        self.thread = Mythread(self._queue)
        self.thread.start()
        self.update()
        
    def update(self):
        if not self.thread.is_alive() and self._queue.empty():
            return
        while not self._queue.empty():
            self.bar += self._queue.get()
        #print('updated : ',self.bar)
        label.configure(text = str(self.bar) + '%')
        frame.after(1000, self.update)

app = tk.Tk()
frame = tk.Frame(app)
frame.grid(row = 0, column = 0, sticky = 'nsew')

label = tk.Label(frame, text = '0%')
label.pack()

process = Process(100, frame)
app.mainloop()
        
        
