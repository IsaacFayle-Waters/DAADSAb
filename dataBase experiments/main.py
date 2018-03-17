import sqlite3
import csv

MalePlayerData = sqlite3.connect('data\MalePlayerData')

cursor = MalePlayerData.cursor()
cursor.execute('''CREATE TABLE `MalePlayerData` ( `name` TEXT, `tempScore` INTEGER, `totalScore` INTEGER, `prizeMoney` INTEGER, `numberOfWins` INTEGER, `totalNumberOfGames` INTEGER )''')

#playerData.commit()
test = 4
with open('data\providedFiles\MALE_PLAYER_LIST.csv',"r") as playerList:
    playerReader = csv.reader(playerList, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for player in playerReader:
        cursor.execute('''INSERT INTO MalePlayerData(name) VALUES(?) ''',(player))

        MalePlayerData.commit()
MalePlayerData.close()
