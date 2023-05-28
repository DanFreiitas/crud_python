import sqlite3 as lite

con = lite.connect('dadod.db')

with con:
    cur = con.cursor()
 
    cur.execute('CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, senha TEXT, telefone TEXT, cpf TEXT, endereco TEXT, estado TEXT)')
con.close()