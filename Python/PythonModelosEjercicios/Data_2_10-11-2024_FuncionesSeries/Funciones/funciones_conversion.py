def dec_hexa(num):
    hexadecimal=''
    while (num!=0):
        dig= num % 16
        num=  num // 16
        dig= str(dig)
        match dig:
            case '10': dig='A' 
            case '11': dig='B' 
            case '12': dig='C' 
            case '13': dig='D' 
            case '14': dig='E' 
            case '15': dig='F'
        hexadecimal= dig+hexadecimal
    return hexadecimal

def hexa_dec(num):
    tamanio=len(num)
    cont=0
    decimal=0
    for dig in range(tamanio-1,-1,-1):
        valor=num[dig]

        match valor:
            case 'A': valor=10 
            case 'B': valor=11 
            case 'C': valor=12 
            case 'D': valor=13 
            case 'E': valor=14 
            case 'F': valor=15
        valor=int(valor)
        decimal= decimal +valor*16**cont
        cont+=1
    return(decimal)        
