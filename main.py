import models.connection
from models.connection import conn

import utils.user_utils as user_utils
import utils.game_utils as game_utils
import utils.game_recommendation_utils as game_recommedation_utils
import models.GameRecommendation as GameRecommendation

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

def create_game_matrix(set_of_game_ids, sorted_game_ids):
  game_matrix = []
  for i in range(len(sorted_game_ids)):
    game_id = sorted_game_ids[i]
    game_vector = [0] * len(sorted_game_ids)
    game_purchase_count = 0
    for j in range(len(set_of_game_ids)):
      if game_id in set_of_game_ids[j]:
        game_purchase_count += 1
        for k in range(len(set_of_game_ids[j])):
          complement_game = set_of_game_ids[j][k]
          if complement_game != game_id:
            game_vector[complement_game - 1] += 1
    if game_purchase_count:
      game_vector = list(map(lambda x: x/game_purchase_count, game_vector))
    game_matrix.append(game_vector)
  return game_matrix

def map_user_to_vector_of_game_id(user_id, user_purchased_game_records, game_count):
  user_vector = [0] * game_count
  index = 0
  while (index < len(user_purchased_game_records)) and (user_purchased_game_records[index][0] < user_id):
    index += 1
  while (index < len(user_purchased_game_records)) and (user_purchased_game_records[index][0] == user_id):
    user_vector[user_purchased_game_records[index][1] - 1] = 1
    index += 1
    
  return user_vector
  
def rank_most_popular_games(set_of_game_ids):
  game_id_to_count = {}
  for i in range(len(set_of_game_ids)):
    game_ids = set_of_game_ids[i]
    for j in range(len(game_ids)):
      game_id = game_ids[j]
      game_count = game_id_to_count.get(game_id)
      if game_count == None:
        game_id_to_count[game_id] = 1
      else:
        game_id_to_count[game_id] = game_count + 1
  
  game_ids = list(game_id_to_count.keys())
  set_game_id_and_count = []
  for i in range(len(game_ids)):
    game_id = game_ids[i]
    count = 0 
    if game_id_to_count[game_id] != None:
      count = game_id_to_count[game_id]
      
    set_game_id_and_count.append([game_id, count])
  set_game_id_and_count.sort(key = lambda x: -x[1])

  return list(map(lambda x: x[0], set_game_id_and_count))

def create_recommed_games(game_matrix, user_vector):
  game_id_with_game_point = []
  for index in range(len(game_matrix)):
    game_id = index + 1
    game_recommend_vector = []
    for _ in range(len(game_matrix)):
      game_recommend_vector.append(game_matrix[_][index])
    point = 0
    for _ in range(len(user_vector)):
      point += user_vector[_] * game_recommend_vector[_]
    game_id_with_game_point.append([game_id, point])
  return game_id_with_game_point

if __name__ == "__main__":
  try:
    GameRecommendation.init_game_recommend_table()
    game_recommedation_utils.clear_recommendation_table()
  
    user_ids = user_utils.get_sorted_user_ids()
    # user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30]
  
    print("user_ids: ", user_ids)
    sorted_game_ids = game_utils.get_sorted_game_ids()
    # sorted_game_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    
    print("sorted_game_ids: ", sorted_game_ids)
    user_purchased_game_records = game_utils.get_user_purchased_game()
    # user_purchased_game_records = [
    #   (1, 1), 
    #   (3, 1), (3, 2), (3, 4), (3, 5), (3, 8), (3, 10), (3, 11), (3, 12), (3, 15), (3, 24), 
    #   (4, 4), (4, 5), (4, 8), (4, 10), 
    #   (25, 1), 
    #   (27, 1), (27, 2), (27, 3), 
    #   (29, 1), (29, 2), (29, 3), (29, 4), (29, 7), 
    #   (30, 3), (30, 4)
    # ]
  
    print("user_purchased_game_records: ", user_purchased_game_records)
    set_of_game_ids = convert_purchased_record_to_set_of_game_ids(user_purchased_game_records)
    # set_of_game_ids = [[1], [1, 2, 4, 5, 8, 10, 11, 12, 15, 24], [4, 5, 8, 10], [1], [1, 2, 3], [1, 2, 3, 4, 7], [3, 4]]
    
    print("")
    print("")
    print("set_of_game_ids: ", set_of_game_ids)
    print("")
    print("")
    game_matrix = create_game_matrix(set_of_game_ids, sorted_game_ids)
    print("game_matrix: ", game_matrix)
    most_popular_games = rank_most_popular_games(set_of_game_ids)
    print("most_popular_games: ", most_popular_games)

    game_recommendation_records = []
    for i in range(len(user_ids)):
    # for i in range(1):
      user_id = user_ids[i]
      user_vector = map_user_to_vector_of_game_id(user_id, user_purchased_game_records, len(sorted_game_ids))
      print("user ", user_id, " has vector: ", user_vector)
      list_of_recommend_game_with_point = list(filter(lambda x: x[1] != 0, create_recommed_games(game_matrix, user_vector)))
      print("user ", user_id, " has recommend game with point: ", list_of_recommend_game_with_point)
      if (len(list_of_recommend_game_with_point)):
        user_id_game_id_point = list(map(lambda x: [user_id, x[0], x[1]], list_of_recommend_game_with_point))
        for _ in range(len(user_id_game_id_point)):
          game_recommendation_records.append(user_id_game_id_point[_])

    game_recommedation_utils.add_records(game_recommendation_records)
  except Exception as e:
    print(str(e))
  finally:
    conn.close()
    print("End")

""" DEBUG RESULT USED FOR COMPUTING LATER (save database query to save money)
user_ids:  [29, 2, 16, 14, 9, 3, 30, 18, 4, 26, 28, 23, 24, 25, 27, 7, 1, 15, 21, 12, 11, 20, 5, 19, 8, 17, 6, 10, 13]
game_ids:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
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