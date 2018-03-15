import sqlite3

playerData = sqlite3.connect('data\MalePlayerData')

cursor = playerData.cursor()

cursor.execute('''SELECT name, tempScore FROM MalePlayerData''')

player = cursor.fetchone()
#cursor.execute(''' ''')
print(player[1])
