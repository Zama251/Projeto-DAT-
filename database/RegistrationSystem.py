from random import randint
from seed import size,name

#SO SERA RODADO UMA VEZ

senhas = []
contas_para_sql = []


def generatorkey() -> None:
    for _ in range(size()):
        senhas.append(randint(1000,9999))


def usergenerator(usuarios:list[str]=name(),senhas:list[int]=senhas) -> list[tuple[str,int]]:
    generatorkey()
    for _ in range(size()):
        user = usuarios[_]
        keys = senhas[_]
        cadatro = (user,keys)
        contas_para_sql.append(cadatro)
       
    return contas_para_sql



