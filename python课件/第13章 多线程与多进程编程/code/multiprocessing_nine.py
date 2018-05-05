from multiprocessing import Process, Event

def f(e, i):
    if e.is_set():
        e.wait()
        print('hello world', i)
        e.clear()
    else:
        e.set()

if __name__ == '__main__':
    e = Event()

    for num in range(10):
        Process(target=f, args=(e,num)).start()
