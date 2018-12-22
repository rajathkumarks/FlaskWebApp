import json
import mysql.connector
from db_config import host
from db_config import user
from db_config import password
from db_config import database

conn = mysql.connector.connect(host=host,user=user,password=password)
cursor = conn.cursor()

sqlquery = '''CREATE DATABASE '''+database
cursor.execute(sqlquery)

sqlquery = """CREATE TABLE student.usermanagement (id INT(5) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))"""
cursor.execute(sqlquery)

conn.commit()

data = {'db_config':[{'host': host, 'user': user, 'password': password, 'database': database}]}
print(json.dumps(data,indent=4))
with open("config.json", "w") as write_file:
    json.dump(data, write_file)
