# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
  CREATE TABLE IF NOT EXISTS songplays( 
    songplay_id SERIAL     PRIMARY KEY   NOT NULL, 
    start_time  timestamp                NOT NULL, 
    user_id     varchar, 
    level       varchar, 
    song_id     varchar , 
    artist_id   varchar , 
    session_id  varchar , 
    location    text, 
    user_agent  varchar);
  """)

user_table_create = ("""
  CREATE TABLE IF NOT EXISTS users (
    user_id     varchar   NOT NULL PRIMARY KEY, 
    first_name  varchar   NOT NULL, 
    last_name   varchar   NOT NULL, 
    gender      varchar, 
    level       varchar   NOT NULL);
  """)

song_table_create = ("""
  CREATE TABLE IF NOT EXISTS songs (
    song_id      varchar   NOT NULL   PRIMARY KEY, 
    title        varchar   NOT NULL, 
    artist_id    varchar   NOT NULL, 
    year         int, 
    duration     FLOAT     NOT NULL);
  """)

artist_table_create = ("""
  CREATE TABLE IF NOT EXISTS artists (
    artist_id    varchar    NOT NULL    PRIMARY KEY, 
    name         varchar    NOT NULL, 
    location     varchar, 
    latitude     varchar, 
    longitude    varchar);
  """)

time_table_create = ("""
  CREATE TABLE IF NOT EXISTS time (
    start_time    timestamp    NOT NULL    PRIMARY KEY, 
    hour          int, 
    day           int, 
    weekday       varchar, 
    week          int, 
    month         int, 
    year          int);
  """)

# INSERT RECORDS

songplay_table_insert = ("""
  INSERT INTO songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \n
  VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """)

user_table_insert = ("""
  INSERT INTO users (user_id, first_name, last_name, gender, level) \n 
  VALUES (%s,%s,%s,%s,%s) \n 
  ON CONFLICT (user_id) 
  DO UPDATE SET LEVEL = excluded.level""")

song_table_insert = ("""
  INSERT INTO songs (song_id, title, artist_id, year, duration) \n 
  VALUES (%s,%s,%s,%s,%s) \n 
  ON CONFLICT (song_id) 
  DO NOTHING""")

artist_table_insert = ("""
  INSERT INTO artists (artist_id, name, location, latitude, longitude) \n 
  VALUES (%s,%s,%s,%s,%s) \n 
  ON CONFLICT (artist_id) 
  DO NOTHING""")


time_table_insert = ("""
  INSERT INTO time (start_time, hour, day, weekday, week, month, year) \n 
  VALUES (%s,%s,%s,%s,%s,%s,%s) \n 
  ON CONFLICT (start_time) 
  DO NOTHING""")

# FIND SONGS

song_select = ("""
  SELECT songs.song_id, artists.artist_id 
  FROM songs   
  JOIN artists ON songs.artist_id =artists.artist_id 
  WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
