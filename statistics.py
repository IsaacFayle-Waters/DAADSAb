import csv
import ranking
import tennisTools
import worldSpecific

statsListPerTornement = []


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


    #print('From Stats: \n')
    #temp until menu function created.
    #zero = 0
    #print('Name ','Wins ','Losses ','1-set ', '2-set', '3-set', '%-Won')
    #for count in range(len(statsList)):
        #print(player[0])
    #    threeSet = int(statsList[count][1]) - (int(statsList[count][3]) + int(statsList[count][4]))
        #(win / (win + lose)) * 100
    #    if statsList[count][1] == 0:
    #        percentage = 0
    #    else:
    #        percentage = (float(statsList[count][1]) / (float(statsList[count][1]) + float(statsList[count][2]))) * 100
        #percentage =
    #    print(statsList[count][0],'   ',statsList[count][1],'   ',statsList[count][2],'   ',statsList[count][3],'   ',statsList[count][4],'   ',threeSet,'   ', percentage)

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

#TODO SEASON STATS
