# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Parvez#01970'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Creat a database
cursorObject.execute("CREATE DATABASE record")

print("All Done!")