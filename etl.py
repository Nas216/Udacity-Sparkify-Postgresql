import os
import glob
import psycopg2
import pandas as pd
import datetime 
from sql_queries import *



def process_song_file(cur, filepath):
    # open song file
    # this should read from song data and populate the songs and artisits tables
    #the arguments are:
    #:param cur: cursur object
    #:param filepath: the location where the data resides
    df = pd.read_json(filepath, lines= True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    #song_data = ()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude'] ].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    # this should read from log data and populate the users, time and songplays tables
    #the arguments are:
    #:param cur: cursur object
    #:param filepath: the location where the data resides 
    df = pd.read_json(filepath, lines= True)

    # filter by NextSong action
    df =df[df['page']=='NextSong'] 

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms')
    year = df['year'] = t.dt.year
    month = df['month'] = t.dt.month
    day = df['day'] = t.dt.day
    week = df['week'] = t.dt.week
    weekday = df['week day'] = t.dt.strftime('%A')
    hour = df['hour'] = t.dt.hour
    
    # insert time data records
    time_data = (t, hour , day, weekday, week, month, year)
    column_labels = ('start_time', 'Hour', 'Day', 'weekday', 'week','month', 'year')
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()