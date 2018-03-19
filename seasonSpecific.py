import csv
import tennisTools

currentWinners = []
#currentWinnersScoreMargin = []
#maxScore = '3'

#function Dealing with manual correction of erroneous non-withdrawral results
def manualCorrection(playerA, playerAscore, playerB, playerBscore, gender):
    #Set gender specifics
    if gender == 'f':
        possibleScore = list(range(tennisTools.womenMaxScore + 1))
        maximumScore = tennisTools.womenMaxScore
    else:
        possibleScore = list(range(tennisTools.menMaxScore + 1))
        maximumScore = tennisTools.menMaxScore
    #Correction Loop until satisfactory score found
    done = False
    while done == False:
        #Input player A score
        choosePlayerAscore = input('Please choose number of sets won by ' + playerA)
        #Validate input. Second Elif probably not needed.
        try:
            if int(choosePlayerAscore) not in possibleScore:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
            elif int(choosePlayerAscore) > maximumScore:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
            else:
                sendPlayerA = choosePlayerAscore
                #print('A chosen')

        except ValueError:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
        #Input player B score
        choosePlayerBscore = input('Please choose number of sets won by ' + playerB)
        #Validate input. Second Elif probably not needed.
        try:
            if int(choosePlayerBscore) not in possibleScore:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
            elif int(choosePlayerBscore) > maximumScore:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
            else:
                sendPlayerB = choosePlayerBscore
                #print('b chosen')

        except ValueError:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
        #Ensure Acceptable winning score for one player. Is x = win and y < win, return, else retry.
        if (int(sendPlayerA) == maximumScore) and (int(sendPlayerB) < maximumScore):
            #print('A wins')
            return sendPlayerA, sendPlayerB
        elif (int(sendPlayerB) == maximumScore) and (int(sendPlayerA) < maximumScore):
            #print('B wins')
            return sendPlayerA, sendPlayerB
        else:
            print('No draws possible. Also, to win, a player must have won 3 sets if male, 2 if female.\nNo score higher than 3 for men, higher than 2 for women, or below zero are allowed\n')
            continue




def menuW(playerA, playerAscore, playerB, playerBscore, gender):

    withdList = ['y', 'n']

    print('\nInvalid result: ' + playerA + ' Sets won:' + playerAscore + ' ' + playerB + ' Sets won:' + playerBscore  )

    if gender == 'f':
        winnerScore = '2'
        looserScore = '1'
    else:
        winnerScore = '3'
        looserScore = '2'

    done = False
    while done == False:

        checkStatus = input('\nHas a player withdrawn? y/n\n').lower()

        if checkStatus not in withdList:
            print('Sorry, that is not a valid choice, please try again')
            continue

        elif checkStatus == 'y':
            confString = 'Was it ' + playerA + '? y/n'
            confirm = input(confString).lower()

            if confirm not in withdList:
                print('\nSorry, that is not a valid choice, please try again\n')
                continue

            elif confirm == 'y':
                playerAscore = looserScore
                playerBscore = winnerScore
                print('Score adjusted')
                return playerAscore, playerBscore
                done = True

            else:
                playerAscore = winnerScore
                playerBscore = looserScore
                print('Score adjusted')
                return playerAscore, playerBscore
                done = True

        else:
            print('No draws possible. Also, to win, a player must have won 3 sets if male, 2 if female.\nNo score higher than 3 for men, higher than 2 for women, or below zero are allowed\n')
            return manualCorrection(playerA, playerAscore, playerB, playerBscore, gender)
            done = True


#New round runner with eroneous score and player withdrwaral options
def runRoundTest(nameOfReadFile, gender):
#Set gender specific score
    if gender == 'f':
        maximumScore = tennisTools.womenMaxScore
        #print('fem')
    else:
        maximumScore = tennisTools.menMaxScore
        #print('mem')
        #print(maximumScore)


    with open(nameOfReadFile, "r") as readRound:
     roundReader = csv.reader(readRound, delimiter =',', quotechar='|')
     for match in roundReader:
         #Deal with erroneous scores.i.e draw
         if (match[1] == match[3]) == True:
             #Manual Correction
             #print('bop')
             match[1], match[3] = menuW(match[0], match[1], match[2], match[3], gender)

         elif (int(match[1]) != maximumScore) and (int(match[3]) != maximumScore):
             #Manual Correction
             #print('bip')
             match[1], match[3] = menuW(match[0], match[1], match[2], match[3], gender)

         #Display Results
         print('Player: ', match[0],' Sets won: ', match[1],' Player: ', match[2],' Sets won: ', match[3])
         #Determine winner, apend list of currentWinners
         if match[1] > match[3]:
             currentWinners.append(match[0])
             currentWinnersScoreMargin.append(int(match[1]) - int(match[3]))
         else:
             currentWinners.append(match[2])
             currentWinnersScoreMargin.append(int(match[3]) - int(match[1]))
    print('\n')

#Simulate past season from file. Choose to update points files, or not. (?)
#def runSeasonFromFile(nameOfSeasonFile):
    #temporary shit for testing

runRoundTest('data\worlds\providedFiles\SEASON_1\\test\TAC1_ROUND_1_MEN.csv', 'm')

#print(currentWinners)
#print(currentWinnersScoreMargin)
#currentWinnersScoreMargin.clear()
#print(currentWinnersScoreMargin)
