#delete operation 
#update player data

import sqlite3

connection = sqlite3.connect("ipl_teams.db")
cursorobj = connection.cursor()
cursorobj.execute("delete from player where gender='f' ")

connection.commit()
connection.close()