import csv
import ranking
import tennisTools
import worldSpecific

statsListPerTornement = []
statsListPerSeason = []


#Works out stats for each player. Wins, Losses, wins by 2-sets, and wins by 1-set
#3-set win margins, and percentage can be calculated from these, and saved else where (Season stats file?)
def playerStatistics(gender):
    #Various globals
    worldFile = worldSpecific.sendPath
    statsList = []
    currentWinners = tennisTools.currentWinners
    currentLosers = tennisTools.currentLosers
    currentWinnersScoreMargin = tennisTools.currentWinnersScoreMargin

    #Select list depending on gender
    if gender == 'f':
        statsFile = worldFile + 'playerStates\FEMALE_PLAYER_STATS.csv'
    elif gender == 'm':
        statsFile = worldFile + 'playerStates\MALE_PLAYER_STATS.csv'

    #Copy file to list
    with open(statsFile, "r") as readStats:
        thesePlayers = csv.reader(readStats, delimiter =',', quotechar='|' )
        for players in thesePlayers:
            statsList.append(players)

    #The Number One!
    one = 1
    #Total wins, TotalLosses, Win Margin-1, win margin-2, for each player
    for i in range(len(statsList)):
        for j in range(len(currentWinners)):
            #If current winner in list for stats, increment win list.
            if currentWinners[j] == statsList[i][0]:
                totalWins = int(statsList[i][1])
                #One Set win margin, two set win margin positions in list
                oneMargin = int(statsList[i][3])
                twoMargin = int(statsList[i][4])
                #Insert/increment Win
                statsList[i].insert(1, totalWins + one)
                statsList[i].pop(2)
                #If won match by one set,increment, elif match won by two sets, increment
                if currentWinnersScoreMargin[j] == one:
                    statsList[i].insert(3, oneMargin + one)
                    statsList[i].pop(4)
                elif currentWinnersScoreMargin[j] == (one + one):
                    statsList[i].insert(4, twoMargin + one)
                    statsList[i].pop(5)
            #If player lost a game, increment the loss list
            elif currentLosers[j] == statsList[i][0]:
                totalLosses = int(statsList[i][2])
                statsList[i].insert(2, totalLosses + one)
                statsList[i].pop(3)

    global statsListPerTornement
    statsListPerTornement = statsList


    #Write back to file
    with open(statsFile, "w", newline='') as writeStatsBack:
        writeStats = csv.writer(writeStatsBack, delimiter =',', quotechar='|')
        for players in range(len(statsList)):
            writeStats.writerow(statsList[players])

#Display and calculate non-written stats
def viewStatsCurrentTornement():
    statsList = statsListPerTornement
    #Display stats
    print('Name ','Wins ','Losses ','1-set ', '2-set', '3-set', '%-Won')
    for count in range(len(statsList)):
        #Calculate three set win margin: threeSet = totalWins - (oneSet + twoSet)
        threeSet = int(statsList[count][1]) - (int(statsList[count][3]) + int(statsList[count][4]))
        #Calculate percentage of wins, do not divide by zero: percentage = (Total wins / (total games played)) * 100
        if statsList[count][1] == 0:
            percentage = 0
        else:
            percentage = (float(statsList[count][1]) / (float(statsList[count][1]) + float(statsList[count][2]))) * 100
        #Display
        print(statsList[count][0],'   ',statsList[count][1],'   ',statsList[count][2],'   ',statsList[count][3],'   ',statsList[count][4],'   ',threeSet,'   ', round(percentage, 2))

def viewStatsCurrentSeason():
    statsList = statsListPerSeason
    #Display stats
    print('Name ','Wins ','Losses ','1-set ', '2-set', '3-set', '%-Won')
    for count in range(len(statsList)):
        #Calculate three set win margin: threeSet = totalWins - (oneSet + twoSet)
        threeSet = int(statsList[count][1]) - (int(statsList[count][3]) + int(statsList[count][4]))
        #Calculate percentage of wins, do not divide by zero: percentage = (Total wins / (total games played)) * 100
        if statsList[count][1] == 0:
            percentage = 0
        else:
            percentage = (float(statsList[count][1]) / (float(statsList[count][1]) + float(statsList[count][2]))) * 100
        #Display
        print(statsList[count][0],'   ',statsList[count][1],'   ',statsList[count][2],'   ',statsList[count][3],'   ',statsList[count][4],'   ',threeSet,'   ', round(percentage, 2))

    #Find max Winner
    maxWinner = statsList[0][1]
    max = int(statsList[0][1])
    for count in range(len(statsList)):
        if int(statsList[count][1]) > max:
            max = int(statsList[count][1])
            maxWinner = statsList[count]

    #Find max loser
    maxLoser = statsList[0][2]
    maxL = int(statsList[0][2])
    for count in range(len(statsList)):
        if int(statsList[count][2]) > maxL:
            maxL = int(statsList[count][2])
            maxLoser = statsList[count]

    print('\nPlayer with most wins this season: ', maxWinner)
    print('Player with most losses this season: ', maxLoser)#TODO FIX THIS. DOESN'T WORK.

def updateSeasonStatsClearTemp(gender):
    worldFile = worldSpecific.sendPath
    statsList = []
    resetList = []
    zero = 0

    if gender == 'f':
        statsFile = worldFile + 'playerStates\FEMALE_PLAYER_STATS_OVERALL.csv'
        statsFileTemp = worldFile + 'playerStates\FEMALE_PLAYER_STATS.csv'
    elif gender == 'm':
        statsFile = worldFile + 'playerStates\MALE_PLAYER_STATS_OVERALL.csv'
        statsFileTemp = worldFile + 'playerStates\MALE_PLAYER_STATS.csv'


    #read in overallPointsFile
    with open(statsFile, "r") as readStats:
        thesePlayers = csv.reader(readStats, delimiter =',', quotechar='|' )
        for players in thesePlayers:
            statsList.append(players)
            resetList.append([zero])

    #insert tempstats + overall stats to overallPointsFile
    for i in range(len(statsListPerTornement)):
        tempCurrentOne = int(statsListPerTornement[i][1]) + int(statsList[i][1])
        tempCurrentTwo = int(statsListPerTornement[i][2]) + int(statsList[i][2])
        tempCurrentThree = int(statsListPerTornement[i][3]) + int(statsList[i][3])
        tempCurrentFour = int(statsListPerTornement[i][4]) + int(statsList[i][4])
        #Insert combined scores
        statsList[i].insert(1, tempCurrentOne)
        statsList[i].pop(2)
        statsList[i].insert(2, tempCurrentTwo)
        statsList[i].pop(3)
        statsList[i].insert(3, tempCurrentThree)
        statsList[i].pop(4)
        statsList[i].insert(4, tempCurrentFour)
        statsList[i].pop(5)
        #Set reset list
        tempName = statsList[i][0]
        resetList[i].insert(0,tempName)
        resetList[i].pop(1)
        resetList[i].insert(1, zero)
        resetList[i].insert(2, zero)
        resetList[i].insert(3, zero)
        resetList[i].insert(4, zero)

    global statsListPerSeason
    statsListPerSeason = statsList

    #Write back
    with open(statsFile, "w", newline='') as writeStatsBack:
        writeStats = csv.writer(writeStatsBack, delimiter =',', quotechar='|')
        for players in range(len(statsList)):
            writeStats.writerow(statsList[players])

    #clear temp
    with open(statsFileTemp, "w", newline='') as writeStatsBackReset:
        writeStats = csv.writer(writeStatsBackReset, delimiter =',', quotechar='|')
        for players in range(len(resetList)):
            writeStats.writerow(resetList[players])


    statsListPerTornement.clear()
