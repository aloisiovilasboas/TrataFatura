import json

my_list = [];





with open('data.txt') as f:
     lines = f.readlines() # list containing lines of file
    
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
                elif "SubTotal" in line:
                    print(line)
                    acabou = True
                elif "Compras parceladas" in line:
                    print(line)
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
                            valorusd = line[69:81].strip()
        #                d = {} # dictionary to store file data (each line)
                        
        #             for index, elem in enumerate(data):
        #                 d[columns[index]] = data[index]

                    my_list.append([date,descricao,parcela,cidade,pais,valorbrl,valorusd]) # append dictionary to list
            i=i+1

# pretty printing list of dictionaries
print(my_list)