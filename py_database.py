
import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_doctypes(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_dox TEXT)")
    conn.commit()



conn = sqlite3.connect('test.db')

# tuple of names
filelist_tuple = ('information.docx','myMovie.mpg','date.pdf', \
                  'myImage.png','myPhoto.jpg'
                  'Hello.txt','World.txt',)

# loop through the tuple to find doc types that end with .txt
for x in filelist_tuple:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_doctypes (col_dox) VALUES (?)",(x,))
            print(x)




conn.close()
