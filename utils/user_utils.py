import models.connection
from models.connection import conn

def get_sorted_user_ids():
  cursor = conn.cursor()
  cursor.execute('SELECT id FROM user ORDER BY id')
  rows = cursor.fetchall()
  cursor.close()
  return list(map(lambda x: x[0], rows))