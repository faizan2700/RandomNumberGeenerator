import time
import threading
import queue
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class MyThread(threading.Thread):
    def __init__(self, queue, n_tasks):
        threading.Thread.__init__(self)
        self._queue = queue
        self._max = n_tasks

    def run(self):
        for i in range(self._max):
            # simulate a task 
            time.sleep(1)
            # put something in the data queue
            self._queue.put(1)


class MyWindow(Gtk.Window):
    def __init__(self, n_tasks):
        Gtk.Window.__init__(self)

        # max and current number of tasks
        self._max = n_tasks
        self._curr = 0

        # queue to share data between threads
        self._queue = queue.Queue()

        # gui: progressbar
        self._bar = Gtk.ProgressBar(show_text=True)
        self.add(self._bar)
        self.connect('destroy', Gtk.main_quit)

        # install timer event to check the queue for new data from the thread
        GLib.timeout_add(interval=250, function=self._on_timer)
        # start the thread
        self._thread = MyThread(self._queue, self._max)
        self._thread.start()

    def _on_timer(self):
        # if the thread is dead and no more data available...
        if not self._thread.is_alive() and self._queue.empty():
            # ...end the timer
            return False

        # if data available
        while not self._queue.empty():
            # read data from the thread
            self._curr += self._queue.get()
            # update the progressbar
            self._bar.set_fraction(self._curr / self._max)

        # keep the timer alive
        return True

if __name__ == '__main__':
    win = MyWindow(30)
    win.show_all()
    Gtk.main()
