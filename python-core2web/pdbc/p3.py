#fetching data from table

import sqlite3

connection = sqlite3.connect("ipl_teams.db")

cursorobj = connection.cursor()

cursorobj.execute("select * from player where teamName = 'rcb' ")

playerdata = cursorobj.fetchall()

for i in playerdata:
    print(i)