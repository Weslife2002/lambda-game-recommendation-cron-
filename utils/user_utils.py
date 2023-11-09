import models.connection
from models.connection import conn

def get_user_ids():
  cursor = conn.cursor()
  cursor.execute('SELECT id FROM user')
  rows = cursor.fetchall()
  cursor.close()
  return list(map(lambda x: x[0], rows))