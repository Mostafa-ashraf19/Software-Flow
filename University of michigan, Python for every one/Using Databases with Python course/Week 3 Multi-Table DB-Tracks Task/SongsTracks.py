import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('TracksDB.sqlite')
commnd = conn.cursor()

filenm = input('file name:  ')
if len(filenm) < 2 : filenm='Library.xml'

filehandle = open(filenm)
root = ET.parse(filehandle)
all = root.findall('dict/dict/dict')

def lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

class communcationwithDB:
   
    def deltables(self,flag,OurText,c=commnd):
        if(flag == 1):
            c.executescript(OurText) 
            conn.commit()
        else:
            return       
    def createtable(self,OurText,c=commnd):
        c.executescript(OurText)
    def inserttrack(self,Trackname,
                    rating,len,count,album_id,genre_id,TBname='Tracks',c = commnd):
        c.execute('INSERT INTO '+TBname+
        '(title,rating,len,count,album_id,genre_id) VALUES(?,?,?,?,?,?)',
        (Trackname,rating,len,count,album_id,genre_id))
    def __del__(self):
        conn.commit()
        conn.close()
    def insertalbum(self,album_title,
                    artist_id,TBname = 'Album',c=commnd):
        c.execute('INSERT INTO '+TBname+'(title,Artist_id) VALUES(?,?)',
        (album_title,artist_id))
    def insertgenre(self,genre_name,TBname = 'genre',c=commnd):
        c.execute('INSERT INTO '+TBname+'(name) VALUES(?)',(genre_name,))
    def insertartist(self,artist_name,TBname = 'Artist',c=commnd):
        c.execute('INSERT INTO '+TBname+'(name) VALUES(?)',
        (artist_name,))

flag= 1
trackdb = communcationwithDB()

trackdb.deltables(flag,''' 
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS Tracks;
''')

trackdb.createtable(''' 
CREATE TABLE IF NOT EXISTS Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,rating INTEGER,count INTEGER
);
CREATE TABLE IF NOT EXISTS Album
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    Artist_id INTEGER 
);
CREATE TABLE IF NOT EXISTS Artist
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE IF NOT EXISTS genre
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
''')

for entry in all:
    if(lookup(entry,'Track ID') is None): continue

    name = lookup(entry,'Name')
    artist = lookup(entry,'Artist')
    album = lookup(entry,'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry,'Genre')

    if name is None or artist is None or album is None or genre is None : continue
    print(name, artist, album, count, rating, length)

    commnd.execute(''' 
    INSERT OR IGNORE INTO Artist(name) VALUES(?) 
    ''',(artist,))
    commnd.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = commnd.fetchone()[0]

    commnd.execute(''' 
    INSERT OR IGNORE INTO Album(title,Artist_id) VALUES(?,?)
    ''',(album,artist_id))
    commnd.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = commnd.fetchone()[0]

    commnd.execute(''' 
    INSERT OR IGNORE INTO genre(name) VALUES(?)
    ''',(genre,))
    commnd.execute('''SELECT id From genre WHERE name = ? ''',(genre,))
    genre_id = commnd.fetchone()[0]
    
    commnd.execute(''' 
    INSERT OR REPLACE INTO Track(title,album_id,genre_id,len,rating,count) VALUES(?,?,?,?,?,?) 
    ''',(name,album_id,genre_id,length,rating,count))
