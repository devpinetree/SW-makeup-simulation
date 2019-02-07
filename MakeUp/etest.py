with open('getEmail.txt','r') as f:
    for line in f:
        x=line.index('@')
        a=line[:x]
        print a
        b=line[x+1:]
        print b
   
