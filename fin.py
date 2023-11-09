import customtkinter
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTk

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

 # Widgets de login
        self.username_label = CTkLabel(self, text="Username:")
        

        self.username_entry = CTkEntry(self)
        

        self.password_label = CTkLabel(self, text="Password:")
        

        self.password_entry = CTkEntry(self, show="*")
        

        self.login_button = CTkButton(self, text="Login", command=self.login)

    def login(self):
        # Valida as credenciais
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            self.master.destroy()
            # Abrir janela principal após o login
            # Exemplo:
            #MainApp()
        else:
            print("Erro de login", "Credenciais inválidas.")        

        



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()