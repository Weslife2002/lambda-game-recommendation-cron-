import models.connection
from models.connection import conn

def clear_recommendation_table():
  cursor = conn.cursor()
  cursor.execute('DELETE * FROM game_recommendation')
  rows = cursor.fetchall()
  return list(map(lambda x: x[0], rows))

def add_records(game_recommendation_records):
  values = ", ".join(list(map(lambda record: f"({record[0]}, {record[1]}, {record[2]})" , game_recommendation_records)))
  insertCommand = f"""
  INSERT INTO game_recommendation (userId, gameId, point)
  VALUES
  {values};
  """
  # cursor = conn.cursor()
  # cursor.execute(insertCommand)
  print (insertCommand)