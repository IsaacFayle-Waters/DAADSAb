import csv
import tennisTools
#import menuFunctions
import worldSpecific
import ranking
import statistics
#import resetOverallToZero
#worldFile = worldSpecific.sendPath

#Globals
seasonNumber = None
worldFile = worldSpecific.sendPath
currentSeeds = []

#Check season number
def checkAndInit():
    worldFile = worldSpecific.sendPath
    checkList = []
    #Open list to check number
    with open(worldFile + 'states\SEASON_COMPLETE_CHECK.csv', 'r') as readCheckList:
        checkList = list(csv.reader(readCheckList, delimiter =',', quotechar='|'))
    #Pass number to global
    global seasonNumber
    seasonNumber = checkList[0][1]

def setTornementPlayed(tornement,gender,roundNumber):
    worldFile = worldSpecific.sendPath

    tornementOne = tennisTools.tornementOne
    tornementTwo = tennisTools.tornementTwo
    tornementThree = tennisTools.tornementThree
    tornementFour = tennisTools.tornementFour

    #Depending on round and gender, select index to edit list
    if tornement == tornementOne:
        if gender == 'f':
            index = 2
        elif gender == 'm':
            index = 3
    elif tornement == tornementTwo:
        if gender == 'f':
            index = 4
        elif gender == 'm':
            index = 5
    elif tornement == tornementThree:
        if gender == 'f':
            index = 6
        elif gender == 'm':
            index = 7
    elif tornement == tornementFour:
        if gender == 'f':
            index = 8
        elif gender == 'm':
            index = 9

    #Get season state
    with open(worldFile + 'states\SEASON_COMPLETE_CHECK.csv', 'r') as readCheckList:
        checkList = list(csv.reader(readCheckList, delimiter =',', quotechar='|'))

    #Panic indused, poorly named variables.
    one = 1
    zero = 0
    temp = 0
    temp2 = 0
    #If final round of tornement passed, lock tornement for that gender.
    if roundNumber == '5':
        checkList[index].insert(2,one)
        checkList[index].pop(3)
        #Add together all locks, if = 8 season has finished.
        for checks in range(len(checkList)):
            temp = checkList[checks][2]
            temp2 = temp2 + int(temp)
            #If all locks = 1, season has finished
            if temp2 == 8:
                #Increment seasonNumber by one
                tempSeasonNo = checkList[0][1]
                checkList[0].insert(1, int(tempSeasonNo) + one)
                checkList[0].pop(2)
                #As season over, clear season stats list
                statistics.statsListPerSeason.clear()
                #As season over, set all tornemnet locks back to zero
                for i in range(len(checkList)):
                #print('seasonNumber = ', seasonNumber)
                    if i > one:
                        checkList[i].insert(2,zero)
                        checkList[i].pop(3)



    with open(worldFile + 'states\SEASON_COMPLETE_CHECK.csv',"w",newline='') as writeChecklist:
        writeChecks = csv.writer(writeChecklist, delimiter =',', quotechar='|' )
        for positions in range(len(checkList)):
            writeChecks.writerow(checkList[positions])
    #print(seasonNumber)

#Limit menu options depending on tornements already played
def limitTornementOptions(gender, tornement):
    checkList = []
    #Globs
    worldFile = worldSpecific.sendPath
    tornementOne = tennisTools.tornementOne
    tornementTwo = tennisTools.tornementTwo
    tornementThree = tennisTools.tornementThree
    tornementFour = tennisTools.tornementFour

    #Depending on round and gender, select index to edit list
    if tornement == tornementOne:
        if gender == 'f':
            index = 2
        elif gender == 'm':
            index = 3
    elif tornement == tornementTwo:
        if gender == 'f':
            index = 4
        elif gender == 'm':
            index = 5
    elif tornement == tornementThree:
        if gender == 'f':
            index = 6
        elif gender == 'm':
            index = 7
    elif tornement == tornementFour:
        if gender == 'f':
            index = 8
        elif gender == 'm':
            index = 9

    with open(worldFile + 'states\SEASON_COMPLETE_CHECK.csv', 'r') as readCheckList:
        checkList = list(csv.reader(readCheckList, delimiter =',', quotechar='|'))

    if checkList[index][2] == '1':
        print('NO!')
        return 1
    else:
        return 0

def setSeeds(gender, tornement):
    worldFile = worldSpecific.sendPath
    currentWinners = tennisTools.currentWinners

    tornementOne = tennisTools.tornementOne
    tornementTwo = tennisTools.tornementTwo
    tornementThree = tennisTools.tornementThree
    tornementFour = tennisTools.tornementFour

    seedList = []
    #Round one
    #The first sixteen in a season (based on rankpoints) cannot play each other
    #in the first round of a tournament.

    #Compare current winners with seed file
        #if current winner in seed file increment round number of tornement by one

    #IF SEASON > One
        #COPY SEEDLIST FOR USE IN SEEDING
        #WIPE ORIGINAL AND RE-FILL SEED LIST WITH CURRENT POSITION INFO#TODO

    #SEED fileS
    #NAME, TORN1 (0,0,0,0),TORN2 (0,0,0,0),TORN3 (0,0,0,0),TORN4 (0,0,0,0),
    #Actualy only needs name, torn1, torn2, torn3, torn4,
    if gender == 'f':
        seedFile = worldFile + 'playerStates\FEMALE_PLAYER_SEED.csv'
    elif gender == 'm':
        seedFile = worldFile + 'playerStates\MALE_PLAYER_SEED.csv'

    with open(seedFile, "r") as seedyFile:
        thesePlayers = csv.reader(seedyFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            seedList.append(players)

    #Compare and adjust
    one = 1
    for i in range(len(seedList)):
        for j in range(len(currentWinners)):
            #Increment position if player advances to next round in specific tornement
            if tornement == tornementOne:
                if currentWinners[j] == seedList[i][0]:
                    tempPosition = int(seedList[i][1])
                    seedList[i].insert(1, tempPosition + one)
                    seedList[i].pop(2)
            elif tornement == tornementTwo:
                if currentWinners[j] == seedList[i][0]:
                    tempPosition = int(seedList[i][2])
                    seedList[i].insert(2, tempPosition + one)
                    seedList[i].pop(3)
            elif tornement == tornementThree:
                if currentWinners[j] == seedList[i][0]:
                    tempPosition = int(seedList[i][3])
                    seedList[i].insert(3, tempPosition + one)
                    seedList[i].pop(4)
            elif tornement == tornementFour:
                if currentWinners[j] == seedList[i][0]:
                    tempPosition = int(seedList[i][4])
                    seedList[i].insert(4, tempPosition + one)
                    seedList[i].pop(5)
    #Write back
    with open(seedFile, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(seedList)):
            writePoints.writerow(seedList[players])

def isSeed(tornement,gender,roundNumber):
    worldFile = worldSpecific.sendPath
    tornementOne = tennisTools.tornementOne
    tornementTwo = tennisTools.tornementTwo
    tornementThree = tennisTools.tornementThree
    tornementFour = tennisTools.tornementFour

    seedList = []
    currentSeeds = []

    if gender == 'f':
        seedFile = worldFile + 'playerStates\FEMALE_PLAYER_SEED.csv'
        #fillFile = 'parameters\FEMALE_PLAYER_LIST.csv'
    elif gender == 'm':
        seedFile = worldFile + 'playerStates\MALE_PLAYER_SEED.csv'
        #fillFile = 'parameters\MALE_PLAYER_LIST.csv'

    with open(seedFile, "r") as seedyFile:
        thesePlayers = csv.reader(seedyFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            seedList.append(players)

    #with open(fillFile, "r") as fillyFile:
    #    thesePlayers = csv.reader(fillyFile, delimiter=',', quotechar='|')
    #    for players in thesePlayers:
    #        seedList.append(players)

    #In current tornement
        #if round == 1
            #if position in seedList < 1
                #Player=currentSeed
                #currentSeed.append(player)
        #elif round == 2
            #if position in seedList < 2
                #Player=currentSeed
        #elif round == 3
            #if position in seedList < 3
                #Player=currentSeed
        #elif round == 4
            #if position in seedList < 4
                #Player=currentSeed

    if tornement == tornementOne:
        index = 1
    elif tornement == tornementTwo:
        index = 2
    elif tornement == tornementThree:
        index = 3
    elif tornement == tornementFour:
        index = 4

    round = int(roundNumber)

    for i in range(len(seedList)):
        if int(seedList[i][index]) > round:
            thisPlayer = seedList[i][0]
            currentSeeds.append(thisPlayer)

    print(currentSeeds)








#TODO# DO THIS IF HAVE TIME
#def seasonFromFile():
    #tennisTools.runRoundNew(nameOfFile,selectGender)
    #statistics.playerStatistics(selectGender)
    #ranking.updatePointsCurrentTornement(tornement, str(playRound), selectGender)
    #ranking.updateRankPoints(tornement, str(playRound), selectGender)
    #Determine money owed to each player
    #prizeMoney.calculatePrizeMoney(tornement, str(playRound), selectGender)




    #Naming
    #Season number
    #checkList[0][0] = SeasonNo:
    #checkList[0][1] = 0 (Actual season number)

    #Season complete or not
    #checkList[1][0] = CurrentComplete:
    #checkList[1][1] = 0 or 1 (0 = season not complete. 1 = complete)

    #Tornements in season, taken place yes or no? [3] to [10]
    #checkList[2][0] = TAC1_ROUND_
    #checkList[2][1] = f or m
    #checkList[2][2] = 0 or 1 (Has this tornement taken place? true or false)

#checkAndInit()
