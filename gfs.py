car_stop = True

while True:
    command = input('> ').lower()
    if command == 'start' :
        if car_stop:
            print('car is start')
        else :
            print('car is already started')
    elif command == 'stop':
        print('car is stop')
    elif command == 'help':
        print('''
        start = car is start
        stop = car is stop
        quit = game is over
        ''') 