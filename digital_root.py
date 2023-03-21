def digital_root(n):
    while True:
        number = []                 
        for i in str(n):                 
            number.append(int(i))   
        n = sum(number)             
        if n < 10:                  
            return n
        else:                      
            continue