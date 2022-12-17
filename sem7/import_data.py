def import_data(data):    
    sep=":"
    with open('phone.csv', 'a+') as file:        
        file.write(sep.join(data))
        file.write(f"\n")