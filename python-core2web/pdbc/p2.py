#insert into table player

import sqlite3

connection = sqlite3.connect("ipl_teams.db")
cursorobj = connection.cursor()

player1 = '''insert into player values(18,"virat","rcb","m","ind")'''
player2 = '''insert into player values(45,"rohit","mi","m","ind")'''
player3 = '''insert into player values(333,"kris","rcb","m","west")'''
player4 = '''insert into player values(33,"david","dd","m","aus")'''
player5 = '''insert into player values(41,"smriti","rcb","f","ind")'''

cursorobj.execute(player1)
cursorobj.execute(player2)
cursorobj.execute(player3)
cursorobj.execute(player4)
cursorobj.execute(player5)


connection.commit()
connection.close()