

"""file_to_read = open('media_types.txt','r')
file_to_write = open('media_types.txt','w')
data = file_to_read.read()
data_lines = data.split('\n')[:-1]
for line in data_lines[:-1]:
    #print(line.split('|'))
    fields = line.split('|')
    file_to_write.write("(\'")
    for field in fields[:-1]:
        file_to_write.write(field)
        file_to_write.write("\',\'")
    file_to_write.write(fields[-1])
    file_to_write.write("\'),\n")
fields = data_lines[-1].split('|')
file_to_write.write("(\'")
for field in fields[:-1]:
    file_to_write.write(field)
    file_to_write.write("\',\'")
file_to_write.write(fields[-1])
file_to_write.write("\');\n")
file_to_read.close()
file_to_write.close()"""


"""import sqlite3


conn = sqlite3.connect("chinook2.db")

c = conn.cursor()

c.execute("SELECT * FROM media_types ")

f= open("media_types.txt","w+")
results = str(c.fetchall())


for row in results:
    f.write(row)

conn.close()
#print(c.fetchall())"""


# testDB.albums          testDB.genres          testDB.playlist_track
# testDB.artists         testDB.invoice_items   testDB.playlists
# testDB.customers       testDB.invoices        testDB.tracks
# testDB.employees       testDB.media_types
#
# select * from testDB.albums;
#
# .output albums_sqlite_output.txt
#
# select * from testDB.artists;
#
# .output artists_sqlite_output.txt

import sqlite3
import mysql.connector

#
# connection = sqlite3.connect('chinook2.db')
# cursor = connection.cursor()
# cur.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name")
# results = cur.fetchall()
# table_data = {}
#
#
#
#
#
# cursor.execute("SELECT * FROM media_types")
# media_types = cursor.fetchall()
# connection.commit()
# # Close the connection
# connection.close()
#
# mydb = mysql.connector.connect(
#   host="127.0.0.1",
#   user="u",
#   password="p",
#   database="music_shop"
# )
#
# cursor = mydb.cursor()
#
# for item in media_types:
#     sql = "INSERT INTO media_types (MediaTypeId, Name) VALUES (%s, %s)"
#     val = item
#     cursor.execute(sql, val)
# mydb.commit()
# https://techoverflow.net/2019/10/14/how-to-list-tables-in-sqlite3-database-in-python/


# def tables_in_sqlite_db(conn):
#     cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     tables = [
#         v[0] for v in cursor.fetchall()
#         if v[0] != "sqlite_sequence"
#     ]
#     cursor.close()
#     return tables
#
#
#
# # Open database
# conn = sqlite3.connect('chinook2.db')
# # List tables
# tables = tables_in_sqlite_db(conn)
# # Your code goes here!
# # Example:
# print(tables) # prints ['commands', 'packages']





#https://pypi.org/project/sqlite-dump/
import sqlite3
file_to_write = open('sqlite_dump.txt', 'w')
conn = sqlite3.connect("chinook2.db")
for line in conn.iterdump():
    file_to_write.write(line)
    #print(line)
file_to_write.close()



from pathlib2 import Path
path = Path("sqlite_dump.txt")
text = path.read_text()
text = text.replace('AUTOINCREMENT', 'auto_increment')
path.write_text(text)


# Here a list of ALL the differences in SQL syntax that I know about between the two file formats:
# The lines starting with:
#
# BEGIN TRANSACTION
# COMMIT
# sqlite_sequence
# CREATE UNIQUE INDEX
# are not used in MySQL
#
# SQLite uses CREATE TABLE/INSERT INTO "table_name" and MySQL uses CREATE TABLE/INSERT INTO table_name
# MySQL doesn't use quotes inside the schema definition
# MySQL uses single quotes for strings inside the INSERT INTO clauses
# SQLite and MySQL have different ways of escaping strings inside INSERT INTO clauses
# SQLite uses 't' and 'f' for booleans, MySQL uses 1 and 0
# (a simple regex for this can fail when you have a string like: 'I do, you don't' inside your INSERT INTO)
# SQLLite uses AUTOINCREMENT, MySQL uses AUTO_INCREMENT
