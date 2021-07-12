"""
import mysql.connector
import csv

music_shop = mysql.connector.connect(host='127.0.0.1',
    user='root',
    passwd='passs',
    db='music_shop')



with open("media_types.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter="\t")
    all_value = []
    for row in csvfile:
        value = (row[1], row[2])
        all_value.append(value)
query = "insert into 'media_types'('MediaTypeId', 'Name') values(%s,%s,%s)"

cursor = music_shop.cursor()
cursor.executemany(query, all_value)
music_shop.commit()
"""

"""
cursor = music_shop.cursor()

csv_data = csv.reader('media_types.csv')
for row in csv_data:

    cursor.execute('INSERT INTO media_types(MediaTypeId, \
          Name)' \
          'VALUES("%s", "%s")',
          row)
#close the connection to the database.
music_shop.commit()
cursor.close()
"""

import csv
import pandas as pd

import mysql.connector

conn = music_shop = mysql.connector.connect(host='127.0.0.1',
    user='root',
    passwd='pass',
    db='music_shop',
    allow_local_infile = 'True')

#media_types = pd.read_csv("media_types.csv")
cur = conn.cursor()
#for i,row in media_types.iterrows():
           # sql = "INSERT INTO media_types VALUES (%s,%s,%s,%s,%s)"
            #cursor.execute(sql, tuple(row))
            #print("Record inserted")
            #conn.commit()
#media_types.to_sql('media_types', con = conn, if_exists = 'append', chunksize = 1000,index=False)
#df = pd.read_csv("media_types.csv",sep=',',quotechar='\'',encoding='utf8') # Replace Excel_file_name with your excel sheet name
#df.to_sql('media_types',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name
#file = open('media_types.csv')
#csv_data = csv.reader(file)
#query = "LOAD DATA INFILE '/Users/raitums/Desktop/csv/media_types.csv' INTO TABLE media_types "

#cur.execute(query)

