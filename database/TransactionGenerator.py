from seed import name
from random import randint



user = name()#lista de usuarios so nomes
transaction_for_sql = []

def gerador_de_num() -> tuple[int,int]:
    media_conta = randint(0,20)#quanto mais perto de zero mais altos os valores de transaçoes
    qtd_transaçoes = randint(50,1000)
    return media_conta,qtd_transaçoes

def parametros_for(nome:str,minimo:int,maximo:int,qtd:int):
    for i in range(qtd):
        valor=randint(minimo,maximo)
        id_trans = (nome,valor)
        transaction_for_sql.append(id_trans)

def transactiongenerator():
    for nome in name():
        parametros=gerador_de_num()
        if parametros[0]<2:
            parametros_for(nome,5000,100000,parametros[1])
        if parametros[0]<5:
            parametros_for(nome,5000,50000,parametros[1])
        if parametros[0]<8:
            parametros_for(nome,1000,50000,parametros[1])
        if parametros[0]<11:
            parametros_for(nome,1000,10000,parametros[1])
        if parametros[0]<14:
            parametros_for(nome,500,7800,parametros[1])
        if parametros[0]<17:
            parametros_for(nome,100,5700,parametros[1])
        if parametros[0]<=20:
            parametros_for(nome,0,3500,parametros[1])

    return transaction_for_sql

def gerador_min():
    alternador = randint(0,100)
    if alternador%10==0:
        conta=name()
        conta=conta[randint(0,100)]
        valor=randint(0,1000000)
        return (conta,valor)












