import pandas as pd
from pymongo import MongoClient
import numpy as np
import requests
import time
import re
import json
import csv
import ast


client = MongoClient("mongodb://root:password@localhost:27017/")

db = client["anime"]
collection = db["animelist"]


path = 'C:\\Dataset\\copy.xlsx'
data = pd.read_excel(path, index_col=0, na_values=['[]',' '])

# for _, row in data.iterrows():
#     record = {
#         "anime_id": row["anime_id"].item(),
#         "user_id": row["user_id"].item(),
#         "rating": row["rating"].item()
#     }
#     collection.insert_one(record)
first = data.iloc[458]
# print(first)

# # producers = json.loads(first["producers"].replace("'", "\""))  if pd.notna(first["producers"]) else None
# # genres = json.loads(first["genres"].replace("'", "\""))  if pd.notna(first["genres"]) else None
# studios = ast.literal_eval(first['studios'])  if pd.notna(first["studios"]) else None
# # print(producers)
# # print(genres)
# print(studios)

for id, row in data.iterrows():
    try:
        producers = ast.literal_eval(row["producers"])  if pd.notna(row["producers"]) else None
        genres = ast.literal_eval(row["genres"])  if pd.notna(row["genres"]) else None
        studios = ast.literal_eval(row["studios"])  if pd.notna(row["studios"]) else None
    except:
        print(id)
    
    record = {
        "anime_id": id,
        "title": str(row["title"]) if pd.notna(row["title"]) else None,
        "title_japanese": str(row["title_japanese"]) if pd.notna(row["title_japanese"]) else None,
        "cover": row["cover"] if pd.notna(row["cover"]) else None,
        "type": row["type"] if pd.notna(row["type"]) else None,
        "episodes": row["episodes"] if pd.notna(row["episodes"]) else None,
        "airing": row["airing"] if pd.notna(row["airing"]) else None,
        "aired_from": row["aired_from"] if pd.notna(row["aired_from"]) else None,
        "aired_to": row["aired_to"] if pd.notna(row["aired_to"]) else None,
        "duration": row["duration"] if pd.notna(row["duration"]) else None,
        "synopsis": row["synopsis"] if pd.notna(row["synopsis"]) else None,
        "producers": producers,
        "studios": studios,
        "genres": genres
    }
    # print(record)
    # print(_, row)
    try:
        collection.insert_one(record)
    except:
        print(id)
        print(record)
    # break

# path = 'C:\\Users\\nevsk\\Documents\\AnimeRecommendationApp\\server\\src\\datasets\\left.csv'
# data = pd.read_csv(path, low_memory=True, decimal=',')

# def remove_after_last_dot(text):
#     if text is None:
#         return ''
#     pattern = r"\.[^.]*$"
#     stripped_text = re.sub(pattern, "", text)
#     return stripped_text

# def jikan_get_anime_full_by_id(anime_id):
#     url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"

#     response = requests.get(url)
#     if response.status_code == 200:
#         anime = response.json()['data']
#         return {
#             "anime_id": anime['mal_id'],
#             "title": anime['title'],
#             "title_japanese": anime['title_japanese'],
#             "cover": anime['images']['jpg']['image_url'],
#             "type": anime['type'],
#             "episodes": anime['episodes'],
#             "airing": anime['airing'],
#             "aired_from": anime['aired']['from'],
#             "aired_to": anime['aired']['to'],
#             "duration": anime['duration'],
#             "rating": anime['rating'],
#             "score": anime['score'],
#             "synopsis": remove_after_last_dot(anime['synopsis']),
#             "producers": anime['producers'],
#             "studios": anime['studios'],
#             "genres": anime['genres']
#         }
#     else:
#         return None
    


# anime_data_list = []
# counter = 1

# for anime_id in data['anime_id']:
#     anime_data = jikan_get_anime_full_by_id(anime_id)
#     if anime_data is not None:
#         counter += 1
#         print(counter, anime_id)
#         anime_data_list.append(anime_data)
#         time.sleep(1.5)
#     else:
#         print(f"{anime_id} not found")

  
# df = pd.DataFrame(anime_data_list)
# df.loc[:, "synopsis"] = df["synopsis"].apply(lambda x : x.replace('\n', '\\n'))

# df.to_csv("new_anime_dataset.csv", index=False, lineterminator='')
