from thread import start_new_thread, allocate_lock
num_threads = 0
thread_started = False
lock = allocate_lock()
def heron(a):
    global num_threads, thread_started
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()

    lock.acquire()
    num_threads -= 1
    lock.release()
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))
start_new_thread(heron,(1733,))

while not thread_started:
    pass
while num_threads > 0:
    pass
