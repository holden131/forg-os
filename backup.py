import time
ERROR = 43924893284923849238492
print('booting....')
time.sleep(3)
print('welcome to frog ios!')
time.sleep(0.5)
print('what would you like to do?')
print('use enter key to scroll down')
open = input('open a app')
a1 = input('info')
a2 = input("trun off")
if open > a1:
    print('use enter key to scroll down')
    app1 = input('settings')
    app2 = input('email')
    app3 = input('texting app')
    app4 = input('math app')
    app5 = input('app store')
    if app1 > app2:
        print('HI! this is settings what would you like to do? use enter key to scroll down')
        wifi = input('wifi')
        update = input('check for updates')
        github  = input('github')
        if wifi > update:
            wifiname = input('enter in wifi name:')
            password = input('if it has a password put it in if it dose not have a password put it blank:')
            print('connecting....')
            time.sleep(3)
            print('connected! now reboot')
        if update > wifi:
            print('check for updates at:')
            print('https://github.com/holden131/forg-os')
        if github > update:
            print("github:")
            print('https://github.com/holden131/forg-os')
    if app2 > app1:
        print('This app is unavailable.')
    if app3 > app2:
        print('This app is unavailable.')
    if app4 > app3:
        print('what wolud you like to do?')
        math = input('division')
        math2 = input('add')
        math3 = input('sub')
        math4 = input('multiplication')
        if math > math2:
            print('this is being worked on lol')
        if math2 > math:
            add = input('add:')
            print('+')
            add2 = input('add:')
            print(add+add2+ERROR)
        if math3 > math2:
            print('this is being worked on lol')
        if math4 > math3:
            print('this is being worked on lol')
    if app5 > app4:
        print('This app is unavailable.')
else:
    print('hi this my goofy os and have fun with forg os')
    print('and also if random numbres pop up its because theres an error')
if a2 > a1:
    print('off')