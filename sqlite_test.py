import sqlite3
connection= sqlite3.connect("bank.db")
cursor= connection.cursor()
cursor.execute("""create table user(id integer, name text, balance integer)""")
cursor.execute("""insert into user(id, name, balance) values(1, 'Parth', 5000)""")
connection.commit()
cursor.execute("""select * from user""")
result= cursor.fetchall()
print(result)