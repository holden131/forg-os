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