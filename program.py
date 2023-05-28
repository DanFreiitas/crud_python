from tkinter import CENTER, NSEW, NW, Button, Entry, Tk, Frame, Label, ttk, messagebox
from tkcalendar import Calendar, DateEntry

import view


bgcolor = "#e6e5da"
bgblue = "#5f5df0"
bgwhite = "#f8f8fa"
bggreen = "#0BBA11"
bgred = "#FF540B"
textwhite = "#f8f8fa"
textblack = "#000"
textblue = "#5f5df0"


def logado():

    janela = Tk()
    janela.title("")    
    width = 1043
    height = 453
    
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    
    janela.geometry("%dx%d+%d+%d" % (width, height, x, y))

    
    janela.configure(background=bgcolor)
    janela.resizable(False, False)

    frame_cima = Frame(janela, width=310, height=50, bg=bgblue, relief="flat")
    frame_cima.grid(row=0, column=0)

    frame_baixo = Frame(janela, width=310, height=403, bg=bgwhite, relief="flat")
    frame_baixo.grid(row=1, column=0, sticky="NSEW", padx=0, pady=1)

    frame_direita = Frame(janela, width=588, height=403, bg=bgwhite, relief="flat")
    frame_direita.grid(row=0, column=1, rowspan=2, padx=2, sticky=NSEW)



    nome_app = Label(frame_cima, text="Controle de chamados", anchor=NW,bg=bgblue,fg=textwhite,font=('Ivy 13 bold'))
    nome_app.place(x=10, y=20)

    global tree

    def inserir():
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_telefone.get()
        dia = e_calendario.get()
        estado = e_estado.get()
        sobre = e_sobre.get()

        lista = [nome, email, telefone, dia, estado, sobre]

        if nome == '':
            messagebox.showerror('Erro','O nome não pode estar vazio!')
        else:
            view.inserir_dados(lista)
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

            e_nome.delete(0,'end')
            e_email.delete(0,'end')
            e_telefone.delete(0,'end')
            e_calendario.delete(0,'end')
            e_estado.delete(0,'end')
            e_sobre.delete(0,'end')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    def atualizar():
        try:
            tree_dados = tree.focus()
            tree_dicionario = tree.item(tree_dados)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome.delete(0,'end')
            e_email.delete(0,'end')
            e_telefone.delete(0,'end')
            e_calendario.delete(0,'end')
            e_estado.delete(0,'end')
            e_sobre.delete(0,'end')


            e_nome.insert(0,tree_lista[1])
            e_email.insert(0,tree_lista[2])
            e_telefone.insert(0,tree_lista[3])
            e_calendario.insert(0,tree_lista[4])
            e_estado.insert(0,tree_lista[5])
            e_sobre.insert(0,tree_lista[6])


            def update():
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_telefone.get()
                dia = e_calendario.get()
                estado = e_estado.get()
                sobre = e_sobre.get()

                lista = [nome, email, telefone, dia, estado, sobre, valor_id]

                if nome == '':
                    messagebox.showerror('Erro','O nome não pode estar vazio!')
                else:
                    view.atualizar_dados(lista)
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                    e_nome.delete(0,'end')
                    e_email.delete(0,'end')
                    e_telefone.delete(0,'end')
                    e_calendario.delete(0,'end')
                    e_estado.delete(0,'end')
                    e_sobre.delete(0,'end')

                for widget in frame_direita.winfo_children():
                    widget.destroy()
                mostrar()

            b_confirmar = Button(frame_baixo,command=update, text="Confirmar",bg=bggreen,fg=textwhite,font=('Ivy 9 bold'), width=10, relief='raised', overrelief='ridge')
            b_confirmar.place(x=110, y=300)     

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados da tabela!')    

    def deletar():
        try:
            tree_dados = tree.focus()
            tree_dicionario = tree.item(tree_dados)
            tree_lista = tree_dicionario['values']

            valor_id = [tree_lista[0]]

            view.deletar_dados(valor_id)
            messagebox.showinfo('Sucesso', 'Informações deletadas com sucesso!')

            for widget in frame_direita.winfo_children():
                    widget.destroy()
            mostrar()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados da tabela!')    

    def sair():
        janela.quit()

    b_sair = Button(frame_baixo,command=sair, text="Sair",fg=textblue,font=('Ivy 9 bold'), width=10, relief='flat', overrelief='ridge')
    b_sair.place(x=110, y=370)  

    l_nome = Label(frame_baixo, text="Nome:*", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_nome.place(x=10, y=10)

    e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_nome.place(x=14, y=30, height=32)



    l_email = Label(frame_baixo, text="E-mail:*", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_email.place(x=10, y=63)

    e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_email.place(x=14, y=83, height=32)



    l_telefone = Label(frame_baixo, text="Telefone:*", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_telefone.place(x=10, y=116)

    e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_telefone.place(x=14, y=136, height=32)



    l_calendario = Label(frame_baixo, text="Data da consulta:*", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_calendario.place(x=10, y=169)

    e_calendario = DateEntry(frame_baixo, width=14, justify='left', borderwidth=2, year=2022)
    e_calendario.place(x=14, y=191, height=32)



    l_estado = Label(frame_baixo, text="Estado da consulta:", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_estado.place(x=148, y=169)

    e_estado = Entry(frame_baixo, width=22, justify='left', relief='solid')
    e_estado.place(x=150, y=191, height=32)



    l_sobre = Label(frame_baixo, text="Consulta sobre:", anchor=NW,bg=bgwhite,fg=textblack,font=('Ivy 10 bold'))
    l_sobre.place(x=10, y=224)

    e_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_sobre.place(x=14, y=244, height=32)



    b_inserir = Button(frame_baixo,command=inserir, text="Adicionar",bg=bgblue,fg=textwhite,font=('Ivy 9 bold'), width=10, relief='raised', overrelief='ridge')
    b_inserir.place(x=12, y=330)


    b_atualizar = Button(frame_baixo,command=atualizar, text="Atualizar",bg=bggreen,fg=textwhite,font=('Ivy 9 bold'), width=10, relief='raised', overrelief='ridge')
    b_atualizar.place(x=110, y=330)


    b_deletar = Button(frame_baixo,comman=deletar, text="Deletar",bg=bgred,fg=textwhite,font=('Ivy 9 bold'), width=10, relief='raised', overrelief='ridge')
    b_deletar.place(x=210, y=330)

    def mostrar():

        global tree

        lista = view.mostrar_dados()

        cabecalho_tabela = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


        tree = ttk.Treeview(frame_direita, selectmode="extended", columns=cabecalho_tabela, show="headings")

        vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

        hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        frame_direita.grid_rowconfigure(0, weight=12)


        hd=["nw","nw","nw","nw","nw","center","center"]
        h=[30,170,140,100,120,50,100]
        n=0

        for col in cabecalho_tabela:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in lista:
            tree.insert('', 'end', values=item)



    mostrar()
    janela.mainloop()
