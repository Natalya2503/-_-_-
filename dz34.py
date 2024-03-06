# Создать таблицу "Студенты" с полями: Имя, Фамилия, Возраст, Группа.

import sqlite3 as sq

with sq.connect('students.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
    id_student INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    groups INTEGER
    )""" )
   
cur.execute("INSERT INTO students VALUES (1,'Александр', 'Иванов', 18, 5)"),
cur.execute("INSERT INTO students VAlUES (2,'Василий', 'Николаев', 20, 3)"),
cur.execute("INSERT INTO students VALUES (3,'Антон', 'Белов', 19, 5)")


# Создать таблицу "Книги" с полями: Название, Автор, Год издания, Жанр.

with sq.connect("books1.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS books (
    id_book INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    genre TEXT
    )""")

def add_book(cur, title, author, year, genre):
    if year < 1600 and year > 2024:
        print('Некорректный год')
        return 0
    cur.execute("INSERT INTO books (title, author, year, genre) VALUES(?, ?)", (title, author, year, genre))

title = 'Война и мир'
author = 'Лев Толстой'
year = 1970
genre = 'Роман-эпопея'



    