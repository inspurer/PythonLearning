funcDict = {'1':lambda:print('You input 1'),
            '2':lambda:print('You input 2'),
            '3':lambda:print('You input 3')}

x = input('Input an integer to call different function:')

func = funcDict.get(x, None)
if func:
    func()
else:
    print('Wrong integer.')
