# import tkinter 

# janela = tkinter.Tk()
# janela.geometry("500x300")

# texto = tkinter.Label(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)        

# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(padx=10, pady=10)

# janela.mainloop()

import customtkinter

def clique():
    print('todo')
    
janela = customtkinter.CTk()
janela.geometry("500x300")

texto =customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)      

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)


janela.mainloop()
