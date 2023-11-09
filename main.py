import models.connection
from models.connection import conn

import utils.user_utils as user_utils
import utils.game_utils as game_utils

def convert_purchased_record_to_set_of_game_ids(user_purchased_game_records):
  set_of_game_ids = []
  currentUserId = None
  for i in range(len(user_purchased_game_records)):
    userId = user_purchased_game_records[i][0]
    gameId = user_purchased_game_records[i][1]
    if (userId != currentUserId):
      currentUserId = userId
      set_of_game_ids.append([gameId])
    else:
      set_of_game_ids[-1].append(gameId)

  return set_of_game_ids

def map_game_to_vector_of_other_game_probability(set_of_game_ids, game_ids):
  return []

def map_user_to_vector_of_game_id(user_purchased_game_records):
  return []
  
def rank_most_popular_games(set_of_game_ids):
  return []

def form_recommed_games(user_purchased_game_records):
  return []

if __name__ == "__main__":
  try:
    user_ids = user_utils.get_user_ids()
    print("user_ids: ", user_ids)
    game_ids = game_utils.get_game_ids()
    print("game_ids: ", game_ids)
    user_purchased_game_records = game_utils.get_user_purchased_game()
    print("user_purchased_game_records: ", user_purchased_game_records)
    set_of_game_ids = convert_purchased_record_to_set_of_game_ids(user_purchased_game_records)
    print("set_of_game_ids: ", set_of_game_ids)
  except e:
    print(e)
  finally:
    cursor.close()
    conn.close()

""" DEBUG RESULT USED FOR COMPUTING LATER (save database query to save money)
user_ids:  [29, 2, 16, 14, 9, 3, 30, 18, 4, 26, 28, 23, 24, 25, 27, 7, 1, 15, 21, 12, 11, 20, 5, 19, 8, 17, 6, 10, 13]
game_ids:  [1, 16, 17, 18, 2, 19, 20, 21, 3, 5, 22, 23, 24, 4, 11, 25, 26, 27, 6, 12, 7, 13, 8, 14, 9, 15, 10]
user_purchased_game_records:  [
  (1, 1), 
  (3, 1), (3, 2), (3, 4), (3, 5), (3, 8), (3, 10), (3, 11), (3, 12), (3, 15), (3, 24), 
  (4, 4), (4, 5), (4, 8), (4, 10), 
  (25, 1), 
  (27, 1), (27, 2), (27, 3), 
  (29, 1), (29, 2), (29, 3), (29, 4), (29, 7), 
  (30, 3), (30, 4)
]
set_of_game_ids:  [[1], [1, 2, 4, 5, 8, 10, 11, 12, 15, 24], [4, 5, 8, 10], [1], [1, 2, 3], [1, 2, 3, 4, 7], [3, 4]]
"""