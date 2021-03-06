import tennisTools

def userInputStack(gender, roundNumber):
    #Populate list of Male Players
    listOfMalePlayers = []
    tennisTools.fillPlayerList('parameters\MALE_PLAYER_LIST.CSV', listOfMalePlayers)

    #Populate list of female players
    listOfFemalePlayers = []
    tennisTools.fillPlayerList('parameters\FEMALE_PLAYER_LIST.CSV', listOfFemalePlayers)

    playerStack = []

    #Choose gender specific lists and variables, depending on round
    if gender == 'f':
        if roundNumber == '1':
            playerStack = listOfFemalePlayers
        else:
            playerStack = tennisTools.currentWinners
        #List of acceptable scores
        possibleScore = list(range(tennisTools.womenMaxScore + 1))
        #Minimum score of combined points for a match
        minScore = tennisTools.womenMaxScore
    elif gender == 'm':
        if roundNumber == '1':
           playerStack = listOfMalePlayers
        else:
            playerStack = tennisTools.currentWinners
        #List of acceptable scores
        possibleScore = list(range(tennisTools.menMaxScore + 1))
        #Minimum score of combined points for a match
        minScore = tennisTools.menMaxScore

    #Initialize list for scores
    roundReturn = [[[],[]] for x in range(len(playerStack))]

    #Keep position for adding players to array. If incremented, advance through round.
    count = 0

    #While players still available
    while playerStack:

        #Display choice
        print(playerStack)

        #Determine which player, A or B
        if count % 2 == 0:
            playerAorB = 'A'
            matchComplete = False
        else:
            playerAorB = 'B'
            matchComplete = True

        #user input player
        choosePlayer = input('Please Pick Player ' + playerAorB + ' from the above list').upper()

        #if player available, remove player from stack, and add to round. If not, retry.
        try:
            playerStack.remove(choosePlayer)
            roundReturn[count][0].append(choosePlayer)

        except ValueError:
            print('Player not available. Please choose a player from the following:')
            continue

        done = False
        #While an acceptable score has not been chosen
        while done == False:

            #User input score
            chooseScore = input('Please choose number of sets won by Player ' + playerAorB)

            try:
                #Is choice in list of acceptable choices? If not, retry.
                if int(chooseScore) not in possibleScore:
                    print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                    continue
                else:
                    #Acceptable. Append List, end loop.
                    roundReturn[count][1].append(int(chooseScore))
                    done = True
            except ValueError:
                print('Please choose an excepted score. 0 to 2 for females. 0 to 3 for males')
                continue
        #Advance
        count = count + 1
        #Check if last score entered was final score of match
        #if matchComplete == True:
            #TODO Logic: Needs to now Question wether an inproper result is due to player withdraw.
            #Maybe do this at this stage, or write function to check scores afterwards. Check spec.

            #if player a score != minScore and playerB != min score. accept = False
            #if (roundReturn[count - 1][1][0] != minScore) and (roundReturn[count][1][0] != minScore):
            #    accept = False
            #else:
            #    accept = True

            #if scores are equal or no one got a winning score, return player B to list of available players, remove player B and their score from round
            #if (roundReturn[count][1] == roundReturn[count - 1][1]) or (accept == False):
            #    print('No draws possible. Also, to win, a player must have won 3 sets if male, 2 if female.')
            #    #Return player to stack of available players
            #    playerStack.insert( count ,choosePlayer)
            #    #pop player and score from round.
            #    roundReturn[count][1].pop()
            #    roundReturn[count][0].pop()
            #    continue
        #    else:
                #Advance
        #        count = count + 1
        #else:
            #Advance
        #    count = count + 1

    #print('RR', roundReturn)
    return roundReturn

#function Dealing with manual correction of erroneous non-withdrawral results
def manualCorrection(playerA, playerAscore, playerB, playerBscore, gender):
    #Set gender specifics
    if gender == 'f' or gender == '_WOMEN':
        possibleScore = list(range(tennisTools.womenMaxScore + 1))
        maximumScore = tennisTools.womenMaxScore
    elif gender == 'm' or gender == '_MEN':
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
