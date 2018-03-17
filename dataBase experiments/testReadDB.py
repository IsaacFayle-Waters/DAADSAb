import sqlite3

zero = 0

playerData = sqlite3.connect('data\MalePlayerData')

cursor = playerData.cursor()

#SELECT INDIVIDUAL, EXAMPLE OF returns: 'MP05', None, None, None, None, None) 
testPlayer = 'MP05'
cursor.execute('''SELECT name, tempScore, totalScore, prizeMoney, numberOfwins, totalNumberOfGames FROM MalePlayerData WHERE name=?''',(testPlayer,))
player = cursor.fetchone()

print(player)

print(cursor.fetchall())


