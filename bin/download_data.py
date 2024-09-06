# I've formated this python script to work.

import requests
import json
import gzip
import shutil
import time
import os
from io import BytesIO

# Insert desired league here (i.e. vct-international, vct-challengers, game-changers)
# e.g. "https://vcthackathon-data.s3.us-west-2.amazonaws.com/vct-international"
# e.g. "https://vcthackathon-data.s3.us-west-2.amazonaws.com/vct-challengers"
# e.g. "https://vcthackathon-data.s3.us-west-2.amazonaws.com/game-changers"
S3_BUCKET_URL = "https://vcthackathon-data.s3.us-west-2.amazonaws.com/vct-international"

def download_gzip_and_write_to_json(file_name):
    if os.path.isfile(f"{file_name}.json"):
      return
    response = requests.get(f"{S3_BUCKET_URL}/{file_name}.json.gz")
    if response.status_code == 200:
      try:
        gzip_bytes = BytesIO(response.content)
        with gzip.GzipFile(fileobj=gzip_bytes, mode="rb") as gzipped_file:
          with open(f"{file_name}.json", 'wb') as output_file:
            shutil.copyfileobj(gzipped_file, output_file)
          print(f"{file_name}.json written")
      except Exception as e:
        print("Error:", e)
    else:
      print(response)
      print(f"Failed to download {file_name}")


def download_esports_files():
  directory = "esports-data"
  if not os.path.exists(directory):
    os.makedirs(directory)

  esports_data_files = ["leagues", "tournaments","players", "teams", "mapping_data"]
  for file_name in esports_data_files:
    download_gzip_and_write_to_json(f"{directory}/{file_name}")


def download_games():
  start_time = time.time()
  with open("esports-data/mapping_data.json", "r") as json_file:
    mappings_data = json.load(json_file)

  directory = "games"
  if not os.path.exists(directory):
    os.makedirs(directory)

  mappings = {
    esports_game["platformGameId"]: esports_game for esports_game in mappings_data
  }

  game_counter = 0

  for esports_game in mappings_data:
    download_gzip_and_write_to_json(f"games/{esports_game['platformGameId']}")
    game_counter += 1
    if game_counter % 10 == 0:
      print(f"----- Processed {game_counter} games, current run time: {round((time.time() - start_time)/60, 2)} minutes")


if __name__ == "__main__":
  download_esports_files()
  download_games()