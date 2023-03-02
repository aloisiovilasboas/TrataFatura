import json
my_list = [];

with open('data.txt') as f:
     lines = f.readlines() # list containing lines of file
    
    # columns = [] # To store column names

     i = 0
     parcelada= False;
     for line in lines:
            
            if line == "         Compras parceladas":
                parcelada = True

            if i>45 and len(line)>0 and line[0].isdigit():
                    
                    descricao = line[10:33].strip()
                    cidade = line[33:47].strip()
                    date = line[:10]
                    d = {} # dictionary to store file data (each line)
                    
    #             for index, elem in enumerate(data):
    #                 d[columns[index]] = data[index]

                    my_list.append(descricao) # append dictionary to list
            i=i+1

# pretty printing list of dictionaries
print(my_list)