import datetime
import pymysql


cnx = pymysql.connect(host='127.0.0.1', user='root', password='root', db='mysql')
cursor = cnx.cursor()

query = ("SELECT user, host from mysql.user")

cursor.execute(query)

for (user, host) in cursor:
    print("User {}, host {}".format(user,host))

cursor.close
cnx.close
