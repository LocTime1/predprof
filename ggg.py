def get_date():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    try:
        query = "SELECT day, month, year FROM data_days"
        cursor.execute(query)

        results = cursor.fetchall()

        need_results = []

        for elem in results:
            need_results.append([str(elem[0]) + '-' + str(elem[1]) + '-' + str(elem[2])])

        return need_results

    finally:
        connection.close()