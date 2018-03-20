import csv
#import tennisTools
#import menuFunctions
#import worldSpecific
#import resetOverallToZero
#worldFile = worldSpecific.sendPath

#Initialise Check files
    #open
    #Add File name

#read season check file (gender, tornement)
    #Check season number
    #

#Test
def checkAndInit():
    checkList = []

    with open('states\SEASON_COMPLETE_CHECK.csv', 'r') as readCheckList:
        checkList = list(csv.reader(readCheckList, delimiter =',', quotechar='|'))

    print(checkList[3][2])
    #Naming
    #checkList[0][0] = file:
    #checkList[0][1] = Null (File Name)

    #Season number
    #checkList[1][0] = SeasonNo:
    #checkList[1][1] = 0 (Actual season number)

    #Season complete or not
    #checkList[2][0] = CurrentComplete:
    #checkList[2][1] = 0 or 1 (0 = season not complete. 1 = complete)

    #Tornements in season, taken place yes or no? [3] to [10]
    #checkList[3][0] = TAC1_ROUND_
    #checkList[3][1] = f or m
    #checkList[3][2] = 0 or 1 (Has this tornement taken place? true or false)

checkAndInit()
