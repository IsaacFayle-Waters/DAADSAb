import os
import shutil

#Select or create a file, and return it's path as string
def fileSelect(choice):
    #Name file. catch OS error.
    if choice == 'N':
        #done = False
        while True:
            try:
                #Name of game file
                worldName = input('Please name your New game: ')
                #os.makedirs('worlds\\' + worldName)

                #String of path. shutil.copytree creates a new directory with the chosen name,
                #And makes a copy of playerStates.
                name = 'worlds\\' + worldName + '\\playerStates'
                shutil.copytree('playerStates', name)

                sendPath = 'worlds\\' + worldName
                return sendPath
                #done = True
            except :#OSError:
                print('Please choose an appropriate File Name. Must not contain: \/:*?"<>| \n ')
    #List existing files and choose which to run
    elif choice == 'E':
        #print(os.listdir("worlds"))
        listOfWorlds = os.listdir("worlds")
        #List files by integer
        i = - 1
        for world in listOfWorlds:
            i = i + 1
            print(i,': ', world)
        #index error, ValueError

        while True:
            try:
                useThis = input ('\nPlease choose Game File from above list by its number: 0,1,2...\n')
                send = 'worlds\\' + listOfWorlds[int(useThis)]
                return send
            except (ValueError, IndexError, OSError) as e:
                print('\nIncorrect choice: Please choose a Game File from above list by its number: 0,1,2...\n')
                continue
