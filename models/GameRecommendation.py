import connection
from connection import conn

def init_game_recommend_database:
  cursor = conn.cursor()
  cursor.execute(
    """ CREATE TABLE IF NOT EXISTS game_recommedation (
    userId INTEGER NOT NULL,
    gameId INTEGER NOT NULL,
    relevant_point INTERGER,
    common_point INTERGER,
    )"""
  )
  cursor.close()