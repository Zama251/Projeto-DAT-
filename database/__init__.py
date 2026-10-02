import TransactionGenerator 
from time import sleep

tabela_transaçoes = TransactionGenerator.transactiongenerator()



def automatizar():
    while True:
        nova_tran = TransactionGenerator.gerador_min()
        tabela_transaçoes.append(nova_tran)
        sleep(180)

