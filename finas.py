from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTk


class LoginApp:
    def __init__(self,master):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Login App")

        # Cria o frame de login com o estilo personalizado
        self.login_frame = CTkFrame(self.master)

        # Widgets de login
        self.username_label = CTkLabel(self.login_frame, text="Username:")
        self.username_label.pack(pady=5)

        self.username_entry = CTkEntry(self.login_frame)
        self.username_entry.pack(pady=5)

        self.password_label = CTkLabel(self.login_frame, text="Password:")
        self.password_label.pack(pady=5)

        self.password_entry = CTkEntry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = CTkButton(self.login_frame, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.login_frame.pack(fill="both", expand=True)

    def login(self):
        # Valida as credenciais
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            self.master.destroy()
            # Abrir janela principal após o login
            # Exemplo:
            main_app = MainApp()
        else:
            print("Erro de login", "Credenciais inválidas.")

class MainApp():
    def __init__(self):
        self.master = CTk()
        self.master.geometry("300x300")
        self.master.title("Login App")

        

        # Cria o frame principal com o estilo personalizado
        self.main_frame = CTkFrame(self.master)
        self.master.mainloop()

        # Adicione widgets para a tela principal aqui
        hello_label = CTkLabel(self.main_frame, text="Bem-vindo à tela principal!")
        hello_label.pack(pady=10)
       

        



root = CTk()
login_app = LoginApp(root)
root.mainloop()
