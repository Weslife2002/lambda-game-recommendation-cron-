import models.connection
from models.connection import conn

def clear_recommendation_table():
  cursor = conn.cursor()
  try:
    cursor.execute('TRUNCATE TABLE game_recommendation')
    conn.commit()  # Commit the changes to the database
  except Exception as e:
    print(e)
  finally:
    cursor.close()

def add_records(game_recommendation_records):
  # values = ", ".join(list(map(lambda record: f"({record[0]}, {record[1]}, {record[2]})" , game_recommendation_records)))
  # insertCommand = f"""
  # INSERT INTO game_recommendation (userId, gameId, point)
  # VALUES
  # {values};
  # """

  print("game_recommendation_records: ", game_recommendation_records)
  cursor = conn.cursor()
  try:
    cursor.executemany(
      "INSERT INTO game_recommendation (userId, gameId, point) VALUES (%s, %s, %s)",
      game_recommendation_records
    )
    conn.commit()
  except Exception as e:
    print(e)
    conn.rollback()
  finally:
    cursor.close()