import webbrowser
import mysql.connector as mc
import os
from time import sleep
from playsound import playsound
from dotenv import load_dotenv

os.system("nohup php -S localhost:8000 -t . > logs/my.log 2>&1 &")

webbrowser.open("localhost:8000")
print("yo")


load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DATABASE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


#with Live(table, refresh_per_second=4):
prevElement = None
while True:

    connection = mc.connect(host=host, database=database, user=user, password=password)
    if connection.is_connected():
        cursor = connection.cursor()

        #sql = "INSERT INTO tasks (pname, room ,pdesc) VALUES (%s, %s, %s)"
        #val = ("TEST name", "TEST room", "TEST description")
        #
        #cursor.execute(sql, val)
        #connection.commit()

        cursor.execute("SELECT * FROM tasks")
        record = cursor.fetchall()
        if record != []:
            if prevElement == None:
                continue
            if prevElement != record[-1]:
                print("new record")
                playsound("assets/notify.wav")
        else:
            pass
    else:
        break
    connection.close()
    sleep(10)

connection.close()