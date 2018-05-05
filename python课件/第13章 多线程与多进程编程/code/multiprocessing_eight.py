from multiprocessing import Process, Manager

def f(d, l, t):
    d['name'] = 'Dong Fuguo'
    d['age'] = 38
    d['sex'] = 'Male'
    d['affiliation'] = 'SDIBT'
    l.reverse()
    t.value = 3
    

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        t = manager.Value('i', 0)

        p = Process(target=f, args=(d, l, t))
        p.start()
        p.join()

        for item in d.items():
            print(item)
        print(l)
        print(t.value)
