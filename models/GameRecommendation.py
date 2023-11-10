import models.connection
from models.connection import conn

def init_game_recommend_table():
  cursor = conn.cursor()
  cursor.execute(
    """ CREATE TABLE IF NOT EXISTS game_recommedation (
    userId INTEGER NOT NULL,
    gameId INTEGER NOT NULL,
    point INTERGER,
    )"""
  )
  cursor.close()