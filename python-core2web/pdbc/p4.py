#update player data

import sqlite3

connection = sqlite3.connect("ipl_teams.db")
cursorobj = connection.cursor()
cursorobj.execute("update player set playerName ='virat kohli' where playerName = 'virat' ")

connection.commit()
connection.close()