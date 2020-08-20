# coding=utf8
import os
import sqlite3
import re
import base64

# path = './'
path = 'G:/map_db/'
loc = 'zzg'


con = sqlite3.connect('satellite.db')
cursor = con.cursor()
# cursor.execute("CREATE TABLE street(tileX integer ,tileY integer ,tileZ integer ,image blob);")


# for root, dirs, files in os.walk(path + loc):
#     print(root, dirs, files)
#     # z = root.split('_')[-1]
#     z = os.path.split(root)[-1]
for z in range(14, 19):
    print('z',  z)
    # for file in files:
    for x in os.listdir(path + loc + '/' + str(z)):
        print('x', x)
        for y in os.listdir(path + loc + '/' + str(z) + '/' + x):

            if not y.endswith('.jpg'):
                continue
            # _, x, y = re.split('_|x', y.rstrip('.png'))
            y = y.strip('.jpg')
            print('y', y)
            with open(os.path.join(path, loc,  str(z), x, y+'.jpg'), 'rb') as f:
                content = f.read()
                sql = f"INSERT INTO street (tileZ,tileX,tileY,image) VALUES (?,?,?,?);"
                print(sql)
                cursor.execute(sql, (z, x, y, sqlite3.Binary(content)))
                con.commit()

con.close()
