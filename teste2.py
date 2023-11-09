import tkinter as tk
import csv

class TabelaCSV(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.tabela = tk.Listbox(self)
        self.tabela.pack()
        
        # Chame o método para carregar o CSV e exibir os dados na tabela
        self.carregar_csv("output_file_path.csv")
    
    def carregar_csv(self, arquivo):
        # Limpar a tabela antes de carregar novos dados
        self.tabela.delete(0, tk.END)
        
        # Abrir o arquivo CSV e ler os dados
        with open(arquivo, "r") as csv_file:
            reader = csv.reader(csv_file)
            for linha in reader:
                # Adicionar cada linha da tabela
                self.tabela.insert(tk.END, "\t".join(linha))

# Criar a janela principal
root = tk.Tk()

# Criar uma instância da classe TabelaCSV
tabela_csv = TabelaCSV(root)
tabela_csv.pack()

# Iniciar o loop principal da aplicação
root.mainloop()
