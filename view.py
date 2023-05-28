import bcrypt
import sqlite3 as lite
from tkinter import messagebox
from program import logado

conn = lite.connect('dadod.db')

def inserir_dados(i):
    with conn:
        cursor = conn.cursor()
        query = '''INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) 
        VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(query,i)   

def mostrar_dados():     
    lista = [] 
    with conn:
        cursor = conn.cursor()
        query = '''SELECT * FROM formulario'''
        cursor.execute(query)
        dados = cursor.fetchall()
        for i in dados:
            lista.append(i)    
    return lista

def atualizar_dados(i):    
    with conn:
        cursor = conn.cursor()
        query = '''UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?'''
        cursor.execute(query,i)  
    
def deletar_dados(i):
    with conn:
        cursor = conn.cursor()
        query = '''DELETE FROM formulario WHERE id=?'''
        cursor.execute(query,i)

def novo_usuario(dados_usuario):
    with conn:
        cursor = conn.cursor()

        def criptografar(senha):
            hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            return hashed.decode('utf-8')

        login = dados_usuario[0]
        senha = dados_usuario[1]
        telefone = dados_usuario[2]
        cpf = dados_usuario[3]
        endereco = dados_usuario[4]
        estado = dados_usuario[5]

        senha = criptografar(senha)
        lista = [login, senha, telefone, cpf, endereco, estado]

        query = '''INSERT INTO usuario (login, senha, telefone, cpf, endereco, estado) VALUES (?, ?, ?, ?, ?, ?)'''

        cursor.execute(query, lista)
        conn.commit()
        cursor.close()
   
def login_in(i):
    conn = lite.connect('dadod.db')

    with conn:
        cursor = conn.cursor()

        query = "SELECT senha FROM usuario WHERE login = ?"
        cursor.execute(query, (i[0],))
        result = cursor.fetchone()

        if result:
            hashed_password = result[0]
            if bcrypt.checkpw(i[1].encode('utf-8'), hashed_password.encode('utf-8')):
               messagebox.showinfo('Sucesso', 'Login efetuado com sucesso')
               logado()
            else:
               messagebox.showerror('Erro', 'Senha inválida')
        else:
            messagebox.showerror('Erro', 'Usuário não localizado')

        cursor.close()