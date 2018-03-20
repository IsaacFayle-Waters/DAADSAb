import os
import shutil

#global sendPath
sendPath = ''

#Select or create a file, and return it's path as string. Copies state files.
def fileSelect(choice):
    #Set Global, so path can be used around the program
    global sendPath
    sendPath
    #If user chooses to create a new game file, input filename, create folder, default state folders..
    if choice == 'N':
        #done = False
        while True:
            try:
                #Name of game file
                worldName = input('Please name your New game: ')
                #String of path. shutil.copytree creates a new directory with the chosen name,
                #And makes a copy of playerStates/states.
                name = 'worlds\\' + worldName + '\\playerStates'
                shutil.copytree('playerStates', name)
                #States. Tornement state.
                name = 'worlds\\' + worldName + '\\states'
                shutil.copytree('states', name)
                #Filename for global use.
                sendPath = 'worlds\\' + worldName + '\\'
                return sendPath
            #Catch OSError
            except :
                print('Please choose an appropriate File Name. Must not contain: \/:*?"<>| \n ')
    #Else if user chooses Existing file, list existing files and choose which to run
    elif choice == 'E':
        #Make list of filenames
        listOfWorlds = os.listdir("worlds")
        #List files by integer from zero up.
        i = - 1
        for world in listOfWorlds:
            i = i + 1
            print(i,': ', world)
        #Choose file, catch out of bounds choce, or non integer choice
        while True:
            try:#If correct selection made, return and set global file name (Return statement needed?)
                useThis = input ('\nPlease choose Game File from above list by its number: 0,1,2...\n')
                #global sendPath
                sendPath = 'worlds\\' + listOfWorlds[int(useThis)] + '\\'
                return sendPath
            except (ValueError, IndexError, OSError) as e:
                print('\nIncorrect choice: Please choose a Game File from above list by its number: 0,1,2...\n')
                continue
