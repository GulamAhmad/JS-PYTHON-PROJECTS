import mysql.connector as mysql
from pygame import mixer
'''

con = mysql.connect(user = 'root', passwd = 'root123',
                    host = 'localhost',
                    db = 'songs')
c = con.cursor()
c.execute("select * from song")
data = c.fetchall()
playsound(data[0][1])
con.close()

'''
mixer.init()
sound = mixer.Sound('laser.wav')
sound.play()
