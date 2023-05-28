from tkinter import Label, Entry, Button, Tk, Label, Frame, messagebox
from view import novo_usuario
from main import iniciar


bgcolor = "#e6e5da"
bgblue = "#5f5df0"
bgwhite = "#f8f8fa"
bggreen = "#0BBA11"
bgred = "#FF540B"
textwhite = "#f8f8fa"
textblack = "#000"
textblue = "#5f5df0"

def new_user():
    root = Tk()
    root.title("Novo usuário")
    root.resizable(False,False)
    
    width = 390
    height = 500
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    
    c_frame = Frame(root, width=400, height=500, bg=bgwhite, relief="flat")
    c_frame.grid(column=0, row=0, columnspan=2)
    
    
    l_user = Label(c_frame, text="Login:* ",bg=bgwhite, font=('Ivy 10 bold'))
    l_user.place(x=50, y=25)
    
    e_user = Entry(c_frame, width=48, justify='left', relief='solid')
    e_user.place(x=51, y=47, height=32)
    
    l_pass = Label(c_frame, text="Senha:* ",bg=bgwhite, font=('Ivy 10 bold'))
    l_pass.place(x=48, y=87)
    
    e_pass = Entry(c_frame, width=48, justify='left', relief='solid', show='*')
    e_pass.place(x=51, y=109, height=32)   
    
    l_telefone = Label(c_frame, text="Telefone: ",bg=bgwhite, font=('Ivy 10 bold'))
    l_telefone.place(x=48, y=150)
    
    e_telefone = Entry(c_frame, width=48, justify='left', relief='solid')
    e_telefone.place(x=51, y=172, height=32)
        
    
    l_cpf = Label(c_frame, text="CPF:* ",bg=bgwhite, font=('Ivy 10 bold'))
    l_cpf.place(x=48, y=213)
    
    e_cpf = Entry(c_frame, width=48, justify='left', relief='solid')
    e_cpf.place(x=51, y=235, height=32)
        
    
    l_endereco = Label(c_frame, text="Endereço: ",bg=bgwhite, font=('Ivy 10 bold'))
    l_endereco.place(x=48, y=276)
    
    e_endereco = Entry(c_frame, width=48, justify='left', relief='solid')
    e_endereco.place(x=51, y=298, height=32)
        
    
    l_estado = Label(c_frame, text="Estado: ",bg=bgwhite, font=('Ivy 10 bold'))
    l_estado.place(x=48, y=339)
    
    e_estado = Entry(c_frame, width=48, justify='left', relief='solid')
    e_estado.place(x=51, y=361, height=32)
    
    b_cancel = Button(c_frame, text="Cancelar", bg=bgwhite, font=('Ivy 10'))
    b_cancel.place(x=210, y=402)
    b_cancel["command"] = root.quit
    
    
    
    def cadastrar():
        login = e_user.get()
        senha = e_pass.get()
        telefone = e_telefone.get()
        cpf = e_cpf.get()
        endereco = e_endereco.get()
        estado = e_estado.get()
        
        lista = [login, senha, telefone, cpf, endereco, estado]
        
        if login == '' or senha == '' or cpf == '':
            messagebox.showerror('Erro', 'Revise os campos obrigatórios (*)')
        elif len(cpf) < 11:
            messagebox.showerror('Erro', 'CPF deve conter 11 dígitos.')
        else:
            novo_usuario(lista)
            messagebox.showinfo('Sucesso', 'Cadastro realizado com sucesso.')
            root.destroy()
            iniciar()
    
    b_cadastrar = Button(c_frame, text="Registrar", bg=bgblue, fg=textwhite, font=('Ivy 10 bold'))
    b_cadastrar.place(x=276, y=402)
    b_cadastrar["command"] = cadastrar
            
    
    
    root.mainloop()
    