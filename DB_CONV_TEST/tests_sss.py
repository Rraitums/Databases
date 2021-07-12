from csv import reader
import csv


import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1',
    user='root',
    passwd='passs',
    db='music_shop')
cursor = mydb.cursor()

# infilemedia_types = open("media_types.csv")
# csvReader = reader(infilemedia_types)
#next(csvReader)
# for row in csvReader:
#     #try:
#     cur.execute("insert into media_types values (%s)", [row[1]])
#     conn.commit()
#     #except:
#         #break

# import pandas as pd
#
# data = pd.read_csv("media_types.csv")
#
# print(data.head())



#query = "LOAD DATA LOCAL INFILE '/Users/raitums/Desktop/csv/media_types.csv' INTO TABLE media_types "
#cur.execute(query)
#conn.commit()


# csv_data = csv.reader('/Users/raitums/Desktop/csv/media_types.csv')
# for row in csv_data:
#
#     cursor.execute('INSERT INTO media_types (MediaTypeId,"
#                    " Name) VALUES("%s", "%s")')
#close the connection to the database.
#media_types = open('media_types.csv', "r")





mydb.commit()
cursor.close()