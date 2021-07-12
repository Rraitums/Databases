import sqlite3
import csv

conn = sqlite3.connect('chinook2.db')
cursor = conn.cursor()

cursor.execute("select * from media_types")
with open("media_types.csv", "w") as csv_file:
    #list of lists \t - Robežu veido spredsheet parasti ar \t
    csv_writer = csv.writer(csv_file, delimiter="\t")
    #.writerow var rakstīt arī tiešos lauku nosaukumu un saturu - ({'first_name': 'Baked', 'last_name': 'Beans'})
    #Lai būtu pirmās rindiņas kā kolonu nosaukumi
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from genres")
with open("genres.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from artists")
with open("artists.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from albums")
with open("albums.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from playlists")
with open("playlists.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from tracks")
with open("tracks.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from playlist_track")
with open("playlist_track.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from employees")
with open("employees.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from customers")
with open("customers.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from invoices")
with open("invoices.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.execute("select * from invoice_items")
with open("invoice_items.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter="\t")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

conn.close()
