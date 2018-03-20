import csv
import tennisTools
#import menuFunctions
import worldSpecific
#import resetOverallToZero
#worldFile = worldSpecific.sendPath

#Globals
seasonNumber = None
worldFile = worldSpecific.sendPath

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


    one = 1
    zero = 0
    temp = 0
    temp2 = 0
    if roundNumber == '5':
        checkList[index].insert(2,one)
        checkList[index].pop(3)
        #Increment Seasonnumber if complete
        for checks in range(len(checkList)):
            temp = checkList[checks][2]
            temp2 = temp2 + int(temp)
            if temp2 == 8:
                #Increment seasonNumber
                tempSeasonNo = checkList[0][1]
                checkList[0].insert(1, int(tempSeasonNo) + one)
                checkList[0].pop(2)


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
