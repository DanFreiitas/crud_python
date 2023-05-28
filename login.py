from gc import callbacks

from tkinter import NW, Tk, Frame, Entry, Label, Button, messagebox

from contrucao import construcao
import sing_up, view, program

bgcolor = "#e6e5da"
bgblue = "#5f5df0"
bgwhite = "#f8f8fa"
bggreen = "#0BBA11"
bgred = "#FF540B"
textwhite = "#f8f8fa"
textblack = "#000"
textblue = "#5f5df0"

def logar():
    root = Tk()
    root.title("Sing in")
    width = 400
    height = 300
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    root.configure(background="white")
    root.resizable(False, False)
    
    def novo_usuario():
        sing_up.new_user()
        root.quit
    
    c_frame = Frame(root, width=400, height=300, bg=bgwhite, relief="flat")
    c_frame.grid(column=0, row=0, columnspan=2)
    
    
    l_user = Label(c_frame, text="Login: ",bg=bgwhite, font=('Ivy 10 bold'))
    l_user.place(x=50, y=25)
    
    e_user = Entry(c_frame, width=48, justify='left', relief='solid')
    e_user.place(x=51, y=47, height=32)
    
    l_pass = Label(c_frame, text="Senha: ",bg=bgwhite, font=('Ivy 10 bold'))
    l_pass.place(x=48, y=87)
    
    e_pass = Entry(c_frame, width=48, justify='left', relief='solid', show='*')
    e_pass.place(x=51, y=109, height=32)
    
    
    def logar():
        login = e_pass.get()
        password = e_pass.get()
        
        lista = [login, password]
        
        if login == '' or password == '':
            messagebox.showerror('Erro', 'Os campos de login e senha devem ser preenchidos')
        else:
            view.login_in(lista)
            
    r_pass = Button(c_frame, text="Esqueceu sua senha? ",bg=bgwhite, fg=textblue, font=('Ivy 7'), relief='flat')
    r_pass.place(x=248, y=145)
    r_pass["command"] = construcao
    
    b_cancel = Button(c_frame, text="Cancelar", width=7, height=2, bg=bgwhite, font=('Ivy 10'))
    b_cancel.place(x=210, y=170)
    b_cancel["command"] = root.quit
    
    b_login = Button(c_frame, text="Entrar", width=7, height=2, bg=bgblue, fg=textwhite, font=('Ivy 10 bold'))
    b_login.place(x=283, y=170)
    b_login["command"] = logar
    
    
    r_pass = Button(c_frame, text="Criar conta",bg=bgwhite, fg=textblue, font=('Ivy 10'), relief='flat')
    r_pass.place(x=152, y=238)
    r_pass["command"] = novo_usuario
    
    
    root.mainloop()
