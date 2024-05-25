import sqlite3;

connection = sqlite3.connect("ipl_teams.db") 

cursorobj = connection.cursor()


createTable = '''

    create table player(
        jerNo integer primary key,
        playerName varchar(20),
        teamName varchar(10),
        gender char(1),
        country varchar(20)
)'''

cursorobj.execute(createTable)
connection.close()