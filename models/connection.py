import os
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import Error

load_dotenv()
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

try:
    conn = mysql.connector.connect(host=MYSQL_HOST, database='sda_assignment', user='backend_dev', password='backend_dev_password')
    if conn.is_connected():
        print('Connect to MySQL database success!')

except Error as e:
    print('Error connecting to MySQL database: ', e)