import sqlite3
import urllib.request , urllib.error , urllib.parse

connect = sqlite3.connect('pro.sqlite')
cursor = connect.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Counts(org TEXT,count INT)
''')

filename = input('file name: ')
try: 
    filehandle = open(filename)
except:
    print('no file')
    quit()
for lines in filehandle:
    lines.lstrip()
    if lines.startswith('From: '):
        words=lines.split(' ')
        dominname = words[1].split('@')
        cursor.execute(''' 
        SELECT org,count FROM Counts WHERE org = ? 
        ''',(dominname[1],))
        row = cursor.fetchone()
        if row is None:
            cursor.execute(''' 
            INSERT INTO Counts(org,count) Values(?,1)
            ''',(dominname[1],))
        else: 
            cursor.execute(''' 
            UPDATA Counts SET count=count+1 WHERE org=?
            ''',(dominname[1],))    

connect.commit()
connect.close()            