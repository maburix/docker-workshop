from flask import Flask
import psycopg2
import os
import socket
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def hello():
    dt = datetime.now()
    try:
        connection = psycopg2.connect(user = "hello_user",
                                password = "hello_pg#1",
                                host = "hello_db",
                                port = "5432",
                                database = "hello_app")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO counter VALUES ( now())')
        connection.commit()
        cursor.execute('SELECT counter FROM counter ORDER BY counter DESC LIMIT 1') 
        visits = cursor.fetchone()[0]

    except psycopg2.Error:
        visits = "<i>cannot connect to PostgreSQL, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>"            "<b>Hostname:</b> {hostname}<br/>"            "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
