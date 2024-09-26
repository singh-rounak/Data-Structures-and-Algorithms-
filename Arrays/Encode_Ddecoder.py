def encoder(string):
    res = ''
    
    for char in string:
        res += str(len(char)) + "#" + char
        
    print(res)
    return res  
    
   

def decoder(str):
    res = []
    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j+=1
        word_length = int(str[i:j])
        res.append(str[j+1:j+1+word_length])
        i = j+1+word_length
        
    print(res)
    return res