import os
import sqlite3
import eyed3


def db_init():

    BASE_DIR = os.getcwd() + '\\tracks'
    listdir = os.listdir(BASE_DIR)

    con = sqlite3.connect('database\music_db.db')
    cur = con.cursor()

    result = cur.execute('''SELECT id, dir FROM all_music''')
    for file in result:
        id, dir = file

        if not os.path.exists(dir):
            cur.execute(f'''DELETE FROM all_music WHERE id = {id}''')
            con.commit()

    for i in list(listdir):

        file = BASE_DIR + f'\{i}'
        audiofile = eyed3.load(file)

        try:
            author, title = audiofile.tag.artist, audiofile.tag.title
        except AttributeError:
            try:
                author, title = i[i.index('-') + 1:].strip, i[:i.index('-')]
            except (IndexError, ValueError):
                author, title = 'Неизвестный', i
        author, title = author.strip('.mp3').replace(
            '\'', ''), title.strip('.mp3').replace('\'', '')
        command = f'''SELECT id FROM all_music WHERE (title = "{title}" AND author = "{author}") OR dir = "{file}" '''
        if not list(cur.execute(command)):

            duration = round(audiofile.info.time_secs)

            cur.execute(
                f'''INSERT INTO all_music (title, author, duration, dir) VALUES ('{title}', '{author}', '{duration}', '{file}') ''')
            con.commit()


db_init()
