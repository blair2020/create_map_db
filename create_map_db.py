# coding=utf8
import os
import sqlite3
import re
import base64

con = sqlite3.connect('satellite.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE street(tileX integer ,tileY integer ,tileZ integer ,image blob);")

path = './'

for root, dirs, files in os.walk(path):
    # print(root, dirs, files)
    z = root.split('_')[-1]
    for file in files:
        if not file.endswith('.Jpeg'):
            continue
        _, x, y = re.split('_|x', file.rstrip('.Jpeg'))
        with open(os.path.join(root, file), 'rb') as f:
            content = f.read()
            sql = f"INSERT INTO street (tileZ,tileX,tileY,image) VALUES (?,?,?,?);"
            print(sql)
            cursor.execute(sql, (z, x, y, sqlite3.Binary(content)))
            con.commit()

con.close()
