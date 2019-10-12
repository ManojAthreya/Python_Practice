#@author:Manoj Athreya A

#DATABASE CREATION

import sqlite3

conn=sqlite3.connect('movie.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Movies')

cur.execute('CREATE TABLE Movies(title TEXT,ratings INTEGER)')
cur.execute('INSERT INTO Movies(title,ratings) VALUES (?,?)',('KGF',5))
cur.execute('INSERT INTO Movies(title,ratings) VALUES (?,?)',('Natasarvabhouma',3))
cur.execute('''INSERT INTO MOVIES VALUES('Yajamana','4')''')
cur.execute('''INSERT INTO MOVIES VALUES('99','3.5')''')
cur.execute('SELECT * FROM Movies')

for row in cur:
    print(row)
    
cur.execute('SELECT title,ratings FROM Movies')
for row in cur:
    print(row)

# =============================================================================
# OUTPUT:
# ('KGF', 5)
# ('Natasarvabhouma', 3)
# ('Yajamana', 4)
# ('99', 3.5)
# =============================================================================
    
cur.execute('SELECT title FROM Movies')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT:
# ('KGF',)
# ('Natasarvabhouma',)
# ('Yajamana',)
# ('99',)
# =============================================================================
cur.execute('SELECT ratings FROM Movies')
for row in cur:
    print(row)
# =============================================================================
# OUTPUT: 
# (5,)
# (3,)
# (4,)
# (3.5,)
# =============================================================================
cur.close()
conn.close()
