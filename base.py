import sqlite3

# Подключение к базе данных
connect = sqlite3.connect("1.db")
curs = connect.cursor()

# Создание таблицы (если не существует)
req_create_table = """
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT
);
"""
curs.execute(req_create_table)
connect.commit()

# Вставка данных
req_insert_data = """
INSERT INTO players (id, username, email) VALUES (2, "Dima2", "dima2@example.com");
"""
curs.execute(req_insert_data)
connect.commit()

# Извлечение данных
req_get_data = """
SELECT * FROM players;
"""
curs.execute(req_get_data)
data = curs.fetchall()
print(data)

# Закрытие cursor и соединения
curs.close()
connect.close()

