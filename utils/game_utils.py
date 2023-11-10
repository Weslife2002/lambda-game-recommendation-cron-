import models.connection
from models.connection import conn

def get_sorted_game_ids():
  cursor = conn.cursor()
  cursor.execute('SELECT id FROM game ORDER BY id')
  rows = cursor.fetchall()
  return list(map(lambda x: x[0], rows))

def get_user_purchased_game():
  cursor = conn.cursor()
  cursor.execute("""
  SELECT DISTINCT billing.userId as userId, game.id as gameId
  FROM game
  INNER JOIN billing_details
  ON billing_details.gameId = game.id
  INNER JOIN billing
  ON billing.id = billing_details.billingId
  ORDER BY userId, gameId
  """)
  rows = cursor.fetchall()
  cursor.close()
  return rows