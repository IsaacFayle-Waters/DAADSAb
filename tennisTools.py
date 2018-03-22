import csv
import menuFunctions
import worldSpecific
import seasonSpecific

from random import*

#defult seed for random
seed()

#global worldFile
worldFile = worldSpecific.sendPath

#stores tempory list of currentWinners to allocate rank points, and to form the fixtures for any subsiquent round.
currentWinners = []
currentWinnersScoreMargin = []
copyForRankPointDifficulty = []
currentLosers = []
seedsTemp = []

#Populate player lists from file
def fillPlayerList(nameOfReadFile, listToFill):
    with open(nameOfReadFile, "r") as playerList:
        playerReader = csv.reader(playerList, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for player in playerReader:
            listToFill.append(' '.join(player))

#Set and simulate fixtures for next round
def setFixtures(nameOfWriteFile, playerList, gender, round):
    seeds = []
    nonSeed = []
    #Help to randomize fixtures by shuffling list
    #shuffle(playerList)

    #CHANGED to reflect seeding. Bit hacky.
    season = int(seasonSpecific.seasonNumber)
    #If in second or subsequent rounds, split list into seeded and non-seeded
    if season > 1:
            if round == 1:
                seeds = seasonSpecific.currentSeeded
                for i in range(len(playerList)):
                    #If player not a seed, add to list of non seeded players
                    if playerList[i] not in seeds:
                        nonSeed.append(playerList[i])
            elif round == 5:
                    pass
            else:
                half = int(len(currentWinners) / 2)
                for players in range(half):
                    seeds.append(currentWinners[players])

                for i in range(len(currentWinners)):
                    if currentWinners[i] not in seeds:
                        nonSeed.append(currentWinners[i])

            #Increase Randomness
            shuffle(seeds)
            shuffle(nonSeed)
            #Display Players in their seeded and non seeded state
            print('Seeds')
            print(seeds)
            print('Non-seeds')
            print(nonSeed)

    #Proceed normanly
    else:
        shuffle(playerList)

    if gender == 'f':
        maxScore = womenMaxScore
    elif gender == 'm':
        maxScore = menMaxScore

    #Find half List size, (halves number of matches per round)
    halfLength = int(len(playerList) / 2)
    #Process matches and write to file
    with open(nameOfWriteFile, "w", newline='') as writeRound:
        matchWriter = csv.writer(writeRound, delimiter =',', quotechar='|' )

        #If more than one season has been played, seeding comes into play
        if season > 1:
            for i in range(halfLength):
                #Set random score in non-erroneous range. (Could include erroneous, as would be caught by newRunRound, but would waste time)
                score = randrange(0,maxScore)
                winScore = maxScore
                if round == 5:
                    playerX = currentWinners[0]
                    playerY = currentWinners[1]
                else:
                    #If seeds list or nonSeed list not empty
                    if seeds:
                        playerX = seeds[0]
                        seeds.pop(0)
                        playerY = seeds[0]
                        seeds.pop(0)
                    #If seeds list empty
                    elif not seeds:
                        #Players from non-seed only
                        playerX = nonSeed[0]
                        nonSeed.pop(0)
                        playerY = nonSeed[0]
                        nonSeed.pop(0)

                #Attempt to remove any pattern in scoring
                moreRandom = randrange(1,3)
                if moreRandom == 1:
                    winner = playerX
                    loser = playerY
                elif moreRandom == 2:
                    winner = playerY
                    loser = playerX
                #Write to file
                if i % 2 == 0:
                    matchWriter.writerow([loser] + [score] + [winner] + [winScore])
                else:
                    matchWriter.writerow([winner] + [winScore] + [loser] + [score])

        else:
        #Write remaining fixtures, psudo randomize scores, and alternate winners
            if gender == 'f':
                for i in range(halfLength):
                    a = randrange(0,womenMaxScore)
                    if i % 2 == 0:
                         matchWriter.writerow([playerList[i]] + [a] + [playerList[i + halfLength]] + [womenMaxScore])
                    else:
                        matchWriter.writerow([playerList[i]] + [womenMaxScore] + [playerList[i + halfLength]] + [a])

            elif gender == 'm':
                for i in range(halfLength):
                    a = randrange(0,menMaxScore)
                    if i % 2 == 0:
                         matchWriter.writerow([playerList[i]] + [a] + [playerList[i + halfLength]] + [menMaxScore])
                    else:
                        matchWriter.writerow([playerList[i]] + [menMaxScore] + [playerList[i + halfLength]] + [a])


def setFixturesFromManual(nameOfWriteFile, playerList, gender):
    clean = []
    #rearrage to fit simple 2d list
    for player in range(len(playerList)):
        a = ''.join(playerList[player][0])
        b = ''.join(str(playerList[player][1])).strip('[]')
        c = a + ',' +  b
        clean.append(c.split(','))

    #write results to file
    with open(nameOfWriteFile, "w", newline='') as writeManualRound:
        matchWriter = csv.writer(writeManualRound, delimiter =',', quotechar='|' )
        for i in range(len(clean)):
            if i % 2 == 0:
                matchWriter.writerow([clean[i][0]] + [clean[i][1]] + [clean[i + 1][0]] + [clean[i + 1][1]] )

#Save information about tornement, for use if program exited mid round.
def checkIfPreviousComplete(tornement, gender):
    #Check tornement in file
    #Check if previous tornement complete = True
    #if True, continue as normal
    #Else if false use last round from round file to initiate next round
    worldFile = worldSpecific.sendPath

    with open(worldFile + 'states\PREVIOUS_ROUND_COMPLETE_CHECK.csv', "r") as checkThisFile:
        tornementPrevious = list(csv.reader(checkThisFile, delimiter =',', quotechar='|'))

        #Determine tornement and gender
        if tornement == tornementOne:
            if gender == 'f':
                index = 0
            elif gender == 'm':
                index = 1
        elif tornement == tornementTwo:
            if gender == 'f':
                index = 2
            elif gender == 'm':
                index = 3
        elif tornement == tornementThree:
            if gender == 'f':
                index = 4
            elif gender == 'm':
                index = 5
        elif tornement == tornementFour:
            if gender == 'f':
                index = 6
            elif gender == 'm':
                index = 7

    #round number to restart from (the number of the previously played, to re-run it)
    global restartRound
    if int(tornementPrevious[index][3]) == 1:
        restartRound = 1
    else:
        restartRound = int(tornementPrevious[index][3])

    roundComplete = tornementPrevious[index][2]
    #print(tornementPrevious[index][0])

    return roundComplete

#Keep track of round, so if program ends before tornement has concluded, the program can start from stop point.
#If tornement reaches end, reset check file
def writePreviousComplete(tornement, gender, roundNumber):
    worldFile = worldSpecific.sendPath
    #Strings for writing verification
    false = 'FALSE'
    true = 'TRUE'
    one = '1'

    #Depending on round and gender, select index to edit list
    if tornement == tornementOne:
        if gender == 'f':
            index = 0
        elif gender == 'm':
            index = 1
    elif tornement == tornementTwo:
        if gender == 'f':
            index = 2
        elif gender == 'm':
            index = 3
    elif tornement == tornementThree:
        if gender == 'f':
            index = 4
        elif gender == 'm':
            index = 5
    elif tornement == tornementFour:
        if gender == 'f':
            index = 6
        elif gender == 'm':
            index = 7

    #Create list of check file
    with open(worldFile + 'states\PREVIOUS_ROUND_COMPLETE_CHECK.csv', "r") as ReadFile:
        tornementPrevious = list(csv.reader(ReadFile, delimiter =',', quotechar='|'))

    with open(worldFile + 'states\PREVIOUS_ROUND_COMPLETE_CHECK.csv', "w", newline='') as checkFile:
        writeCheck = csv.writer(checkFile, delimiter =',', quotechar='|' )
        for tornements in range(len(tornementPrevious)):
            #Round 5. Reset
            if roundNumber == '5':
                #Add change to specific place in list/file
                tornementPrevious[index].pop(2)
                tornementPrevious[index].pop(2)
                tornementPrevious[index].insert(2, true)
                tornementPrevious[index].insert(3, one)
                #writeCheck.writerow([tornementPrevious[tornements][0]] + [tornementPrevious[tornements][1]] + []  )
            #Round 1-4. Edit list as needed
            else:
                #Add change to specific place in list/file
                tornementPrevious[index].pop(2)
                tornementPrevious[index].pop(2)
                tornementPrevious[index].insert(2, false)
                tornementPrevious[index].insert(3, roundNumber)
        #Write to file
            writeCheck.writerow(tornementPrevious[tornements])

#Sets tornement names and points maximums from file (an attempt to avoid hardcoded data/possible paranoia)
def setGlobalsFromFile():

    with open('parameters\TORNEMENT_NAMES_AND_MAX_SCORES.csv', "r") as nameScoreFile:
        readNamesScores = list(csv.reader(nameScoreFile, delimiter =',', quotechar='|'))

    global tornementOne
    tornementOne = str(readNamesScores [0][0])

    global tornementTwo
    tornementTwo = str(readNamesScores [1][0])

    global tornementThree
    tornementThree = str(readNamesScores [2][0])

    global tornementFour
    tornementFour = str(readNamesScores [3][0])

    global menMaxScore
    menMaxScore = int(readNamesScores [4][0])

    global womenMaxScore
    womenMaxScore = int(readNamesScores [5][0])


#Call function here, so as to avoid calling it everywhere else
setGlobalsFromFile()

######################################################
##New functions in complience with coursework Part B##
######################################################

#New version of runRound that can now deal with error score, and player withdrwaral
def runRoundNew(nameOfReadFile, gender):
#Set gender specific score
    if gender == 'f' or gender == '_WOMEN':
        maximumScore = womenMaxScore

    elif gender == 'm' or gender == '_MEN':
        maximumScore = menMaxScore

    with open(nameOfReadFile, "r") as readRound:
     roundReader = csv.reader(readRound, delimiter =',', quotechar='|')
     for match in roundReader:
         #Deal with erroneous draw
         if (match[1] == match[3]) == True:
             #Manual Correction
             #print('bop')
             match[1], match[3] = menuFunctions.menuW(match[0], match[1], match[2], match[3], gender)
        #Deal with any other error score
         elif (int(match[1]) != maximumScore) and (int(match[3]) != maximumScore):
             #Manual Correction
             #print('bip')
             match[1], match[3] = menuFunctions.menuW(match[0], match[1], match[2], match[3], gender)

         #Display Results
         print('Player: ', match[0],' Sets won: ', match[1],' Player: ', match[2],' Sets won: ', match[3])
         #Determine winner, apend list of currentWinners
         if match[1] > match[3]:
             currentWinners.append(match[0])
             currentWinnersScoreMargin.append(int(match[1]) - int(match[3]))
             currentLosers.append(match[2])
         else:
             currentWinners.append(match[2])
             currentWinnersScoreMargin.append(int(match[3]) - int(match[1]))
             currentLosers.append(match[0])
    print('\n')
