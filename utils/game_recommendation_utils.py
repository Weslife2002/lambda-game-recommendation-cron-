import models.connection
from models.connection import conn

def clear_recommendation_table():
  cursor = conn.cursor()
  cursor.execute('DELETE * FROM game_recommendation')
  rows = cursor.fetchall()
  return list(map(lambda x: x[0], rows))

def add_records(game_recommendation_records):
  values = ""
  for _ in range(len(game_recommendation_records)):
    record = game_recommendation_records[_]
    values += f"({record[0]}, {record[1]}, {record[2]}),"
  insertCommand = f"""
  INSERT INTO game_recommendation ()
  VALUES
  {values}
  """
  # cursor = conn.cursor()
  print (insertCommand)
  
    
  print(game_recommendation_records)