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
currentSeeded = []

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
                copyOriginalAndResetOriginal()
                ranking.resetOverAllAtEndOfSeason()
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

#Collect seeds
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
        #NOTE surley overall rank points should be wiped after every season?
        #COPY SEEDLIST FOR USE IN SEEDING
        #WIPE ORIGINAL AND RE-FILL SEED LIST WITH CURRENT POSITION INFO#TODO

    #SEED fileS
    #NAME, TORN1 (0,0,0,0),TORN2 (0,0,0,0),TORN3 (0,0,0,0),TORN4 (0,0,0,0),
    #Actualy only needs name, torn1, torn2, torn3, torn4,
    if gender == 'f':
        if int(seasonNumber) == 1:
            seedFile = worldFile + 'playerStates\TEMP_FEMALE_PLAYER_SEED.csv'
        else:
            seedFile = worldFile + 'playerStates\FEMALE_PLAYER_SEED.csv'
    elif gender == 'm':
        if int(seasonNumber) == 1:
            seedFile = worldFile + 'playerStates\TEMP_MALE_PLAYER_SEED.csv'
        else:
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

#Selects Seeds depending on tornement type, and which round currently playing
def isSeed(tornement,gender,roundNumber):
    worldFile = worldSpecific.sendPath
    tornementOne = tennisTools.tornementOne
    tornementTwo = tennisTools.tornementTwo
    tornementThree = tennisTools.tornementThree
    tornementFour = tennisTools.tornementFour
    currentWinners = tennisTools.currentWinners

    #Ensure round variable is integer
    round = int(roundNumber)

    seedList = []
    currentSeeds = []
    seedTemp = []
    #Gender specifics
    if gender == 'f':
        seedFile = worldFile + 'playerStates\TEMP_FEMALE_PLAYER_SEED.csv'

    elif gender == 'm':
        seedFile = worldFile + 'playerStates\TEMP_MALE_PLAYER_SEED.csv'

    #if round == 1:
        #Read in seedFile
    with open(seedFile, "r") as seedyFile:
        thesePlayers = csv.reader(seedyFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            seedList.append(players)
    #else:
        #seedList = tennisTools.seedsTemp

    #Select position in seed file corresponding with current tornement
    if tornement == tornementOne:
        index = 1
    elif tornement == tornementTwo:
        index = 2
    elif tornement == tornementThree:
        index = 3
    elif tornement == tornementFour:
        index = 4

    #If past tornement position greater than round about to be played,
    #Select player as seed.
    #print('CurrentWinner', currentWinners)
    print(seedList[0][0])

    if round == 1:
        for i in range(len(seedList)):
            if int(seedList[i][index]) > round:
                thisPlayer = seedList[i][0]
                currentSeeds.append(thisPlayer)
                #tennisTools.seedsTemp.append(thisPlayer)


    #print('Please work', currentSeeds)
    global currentSeeded
    currentSeeded = currentSeeds


def copyOriginalAndResetOriginal():
    worldFile = worldSpecific.sendPath
    #originalSeedList = []
    copySeedListFem = []
    copySeedListMen = []


    seedFileFem = worldFile + 'playerStates\FEMALE_PLAYER_SEED.csv'
    previousSeasonSeedingFem = worldFile + 'playerStates\TEMP_FEMALE_PLAYER_SEED.csv'


    seedFileMen = worldFile + 'playerStates\MALE_PLAYER_SEED.csv'
    previousSeasonSeedingMen = worldFile + 'playerStates\TEMP_MALE_PLAYER_SEED.csv'

    #Make original seed matrix to list
    with open(seedFileFem, "r") as seedyFemFile:
        thesePlayers = csv.reader(seedyFemFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            copySeedListFem.append(players)

    with open(seedFileMen, "r") as seedyMenFile:
        thesePlayers = csv.reader(seedyMenFile, delimiter=',', quotechar='|')
        for players in thesePlayers:
            copySeedListMen.append(players)

    #print('Original',copySeedList)
    #Write original to temp (For use in next season)
    with open(previousSeasonSeedingFem, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(copySeedListFem)):
            writePoints.writerow(copySeedListFem[players])

    with open(previousSeasonSeedingMen, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(copySeedListMen)):
            writePoints.writerow(copySeedListMen[players])

    one = 1
    for i in range(len(copySeedListFem)):
        copySeedListFem[i].insert(1,one)
        copySeedListFem[i].pop(2)
        copySeedListFem[i].insert(2,one)
        copySeedListFem[i].pop(3)
        copySeedListFem[i].insert(3,one)
        copySeedListFem[i].pop(4)
        copySeedListFem[i].insert(4,one)
        copySeedListFem[i].pop(5)

    for i in range(len(copySeedListMen)):
        copySeedListMen[i].insert(1,one)
        copySeedListMen[i].pop(2)
        copySeedListMen[i].insert(2,one)
        copySeedListMen[i].pop(3)
        copySeedListMen[i].insert(3,one)
        copySeedListMen[i].pop(4)
        copySeedListMen[i].insert(4,one)
        copySeedListMen[i].pop(5)

        #print('Wiped',copySeedList)
    #Reset orignal to defualt, for fresh season
    with open(seedFileFem, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(copySeedListFem)):
            writePoints.writerow(copySeedListFem[players])

    with open(seedFileMen, "w", newline='') as pointsFile:
        writePoints = csv.writer(pointsFile, delimiter =',', quotechar='|' )
        for players in range(len(copySeedListMen)):
            writePoints.writerow(copySeedListMen[players])





#TODO# DO THIS IF HAVE TIME
#def seasonFromFile():
    #Set Fixtures from file



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
