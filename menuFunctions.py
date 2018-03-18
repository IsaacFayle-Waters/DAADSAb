import sortLists
import prizeMoney
import ranking
import resetOverallToZero
import tennisTools
import manualInput

#Select tornement
def tornementSelector():
    tornDict = {'A': tennisTools.tornementOne, 'B': tennisTools.tornementTwo, 'C': tennisTools.tornementThree, 'D': tennisTools.tornementFour}
    print(tornDict)

    done = False
    while done == False:
        tornChoice = input('Please select a tornement from the list above.').upper()
        if tornChoice not in tornDict:
            print('Sorry, that is not a valid choice, please try again')
            continue
        else:
            return tornDict[tornChoice]
            done = True

#Select gender of players
def genderSelector():
    gendList = ['f', 'm']

    done = False
    while done == False:
        gendChoice = input('Please choose gender of players in tornement. F for female. M for male').lower()
        if gendChoice not in gendList:
            print('Sorry, that is not a valid gender slection. Please choose F for female. M for male ')
            continue
        else:
            return  gendChoice
            done = True

#Select manual input on or off
def manualSelector():
    manList = ['y', 'n']

    done = False
    while done == False:
        manChoice = input('Would you like to input your results manually? y/n').lower()
        if manChoice not in manList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        else:
            return manChoice
            done = True

#Continue to next round
def playNextRound(playRound):
    playChoice = input('Press any button to play next round.')

    return playRound + 1

#Select whether or not to exit
def exitSelector():
    exitList = ['Y', 'N']

    done = False
    while done == False:
        exitChoice = input('Would you like to exit the program? y/n').upper()
        if exitChoice not in exitList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        else:
            return exitChoice
            done = True

#Select to view Prize money or not
def checkPrizeMoney(gender):
    checkPrizeList = ['y','n']

    done = False
    while done == False:
        checkPrize= input('Would you like to view player earnings (assigned on tornement completion)? y/n').lower()
        if checkPrize not in checkPrizeList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        elif checkPrize == 'y':
            prizeMoney.displayWinnings(gender)
            done = True
        else:
            done = True

#Select to view points from round or not
def checkPointsFromRound():
    checkList = ['y','n']

    done = False
    while done == False:
        checkRound = input('Would you like to see the leader board for the current round? y/n').lower()
        if checkRound not in checkList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        elif checkRound == 'y':
            print(sortLists.enterSorting(ranking.copyForSortRankForRound), '\n')
            done = True
        else:
            done = True

#Select to view overall points
def checkOverallRankPoints():
    rankList = ['y','n']

    done = False
    while done == False:
        checkRank = input('Would you like to view overall rank points? y/n').lower()
        if checkRank not in rankList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        elif checkRank == 'y':
            print(sortLists.enterSorting(ranking.copyForSortOverallRank), '\n')
            done = True
        else:
            done = True

#Select whether or not to return files to default
def dataWipe():
    wipeList = ['y', 'n']

    done = False
    while done == False:
        checkWipe = input('Would you like to delete all points data, and set files back to default(Does not delete results files)? y/n').lower()
        if checkWipe not in wipeList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        elif checkWipe == 'y':
            resetOverallToZero.wipeAllData()
            print('Data wiped')
            done = True
        else:
            done = True

#Menu for erroneous results, and player withdrawral
def menuW(playerA, playerAscore, playerB, playerBscore, gender):
    #Possible awnsers to yes no
    withdList = ['y', 'n']
    #Display mistake
    print('\nInvalid result: ' + playerA + ' Sets won:' + playerAscore + ' ' + playerB + ' Sets won:' + playerBscore  )
    #Set gender specific withdraw results
    #print(type(gender))
    #print(type('f'))
    if gender == 'f' or gender == '_WOMEN':
        winnerScore = '2'
        looserScore = '1'
    elif gender == 'm' or gender == '_MEN':
        winnerScore = '3'
        looserScore = '2'

    #Question loop. Possibly doesn't need boolean element, due to return statement
    done = False
    while done == False:
        #Choose direction of re-entry. i.e withdrawral or error
        checkStatus = input('\nHas a player withdrawn? y/n\n').lower()
        #Validation
        if checkStatus not in withdList:
            print('Sorry, that is not a valid choice, please try again')
            continue
        #If player withdrawn: If not A then must be B
        elif checkStatus == 'y':
            confString = 'Was it ' + playerA + '? y/n'
            confirm = input(confString).lower()
            #Validation
            if confirm not in withdList:
                print('\nSorry, that is not a valid choice, please try again\n')
                continue
            #Set A as withdrawn player, return adjusted scores
            elif confirm == 'y':
                playerAscore = looserScore
                playerBscore = winnerScore
                print('Score adjusted')
                return playerAscore, playerBscore
                done = True
            #Else B withdrew, so B gets lower score
            else:
                playerAscore = winnerScore
                playerBscore = looserScore
                print('Score adjusted')
                return playerAscore, playerBscore
                done = True

        else:
            print('No draws possible. Also, to win, a player must have won 3 sets if male, 2 if female.\nNo score higher than 3 for men, higher than 2 for women, or below zero are allowed\n')
            return manualInput.manualCorrection(playerA, playerAscore, playerB, playerBscore, gender)
            done = True
