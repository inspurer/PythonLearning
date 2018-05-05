import multiprocessing as mp

def foo(q):
    q.put('hello world')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    p.join()
    print(q.get())
