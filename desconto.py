valor = float(input('digite o valor '))

def calcula_desconto(valor):
    return valor * 0.95

def aplica_desconto(desconto):
     print(f'o preço com dsconto e R${desconto}')


desconto = calcula_desconto(valor)
aplica_desconto(desconto)
