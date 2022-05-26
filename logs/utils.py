def telefone(num):
    numero = str(num)
    numero = numero.replace('+', '').replace(' ', '').replace('-', '').replace('55', '')
    if not numero.isnumeric():
        return False
    
    print(len(numero))
    return numero

