import sqlite3


def add_day(data):
    name_db = 'data.db'

    connect = sqlite3.connect(name_db)

    cursor = connect.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS data_days (
                id INTEGER PRIMARY KEY,
                day INTEGER,
                month INTEGER,
                year INTEGER
            )
        ''')

    cursor.execute('INSERT INTO data_days (day, month, year) VALUES (?, ?, ?)', data.split('-'))
    result = cursor.fetchone()

    connect.commit()
    connect.close()


def add_info_day(data):
    name_db = 'data.db'

    connect = sqlite3.connect(name_db)

    cursor = connect.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS data_house_day (
                    day TEXT,
                    floor_counts INTEGER,
                    windows_floor_counts INTEGER,
                    lighwindowst_on_info_floor TEXT
                    window_room_count TEXT
                )
            ''')

    data[3] = ' '.join(data[3])
    data[4] = ' '.join(data[4])
    cursor.execute('INSERT INTO data_house_day (day, floor_counts, windows_floor_counts, lighwindowst_on_info_floor, window_room_count) VALUES (?, ?, ?, ?, ?)', data)
    result = cursor.fetchone()
    connect.commit()
    connect.close()


def get_info_day(day):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM data_house_day WHERE day = ?"
        cursor.execute(query, (day,))

        result = cursor.fetchall()

        need_result = []
        for i in range(5):
            if i < 3:
                need_result.append(result[0][i])
            else:
                if i == 3:
                    sp = result[0][i].split(' ')
                    need_sp = []
                    for elem in sp:
                        if elem == 'True':
                            need_sp.append(True)
                        else:
                            need_sp.append(False)
                else:
                    sp = result[0][i].split(' ')
                    need_sp = []
                    for elem in sp:
                        need_sp.append(int(elem))
                need_result.append(need_sp)

        return need_result

    finally:
        connection.close()


print(get_info_day('25-01-23'))

