import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox

import csv

my_list = [];

def filter_file():


    # Abrir janela de seleção de arquivo
    file_path = filedialog.askopenfilename()
    print(file_path)

    output_file_path = os.path.splitext(file_path)[0] + ".csv"

    # Abrir arquivo de entrada e arquivo de saída
    with open(file_path, "r") as input_file, open(output_file_path, "w") as output_file:
        lines = input_file.readlines() # list containing lines of file
        # columns = [] # To store column names
        i = 0
        parcelada= False;
        acabou = False;
        my_list.append(['date','descricao','parcela','cidade','pais','valorbrl','valorusd'])
        for line in lines:
            if not acabou:
                if line.strip() == "":
                    if parcelada:
                            parcelada=False
                elif " Total" in line and not line[0].isdigit() :
                    acabou = True
                elif "Compras parceladas" in line:
                    parcelada = True
                elif i>45 and len(line)>0 and line[0].isdigit():
                    if parcelada:
                            date = line[:10]
                            descricao = line[10:24].strip()
                            parcela = line[29:34].strip()
                            cidade = line[35:47].strip()
                            pais = line[47:49].strip()
                            valorbrl = line[49:69].strip()
                            valorusd = line[69:81].strip()
                    else:
                            date = line[:10]
                            descricao = line[10:33].strip()
                            parcela = ""
                            cidade = line[33:47].strip()
                            pais = line[47:49].strip()
                            valorbrl = line[49:69].strip()
                            valorbrlLimpo = valorbrl.replace(',','.')
                            valorusd = line[69:81].strip()
                            valorusdlimpo = valorusd.replace(',','.')
                    my_list.append([date,descricao,parcela,cidade,pais,valorbrlLimpo,valorusdlimpo])      
            i=i+1
        writer = csv.writer(output_file, lineterminator='\n')
        for row in my_list:
            writer.writerow(row)
        messagebox.showinfo("Arquivo Gerado", f"O arquivo CSV foi gerado com sucesso!\nNome do arquivo: {output_file_path}")    
    #output_file.writelines(my_list)

# Criar janela principal
root = tk.Tk()
root.geometry('400x100+300+300')
root.title('Trata Fatura BB 2023 (não oficial)')

# Criar botão de filtragem de arquivo
filter_button = tk.Button(root, text="Selecione o Arquivo", command=filter_file)
filter_button.pack()

# Iniciar loop principal da janela
root.mainloop()