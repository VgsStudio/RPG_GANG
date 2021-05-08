from discord.ext import commands

class Personagem():
    def __init__(self, nome, vitalidade, força, observaçao, destreza, inteligencia, carisma, sorte, poder):
        self.atributo = {'nome': nome, 'vitalidade': vitalidade, 'força': força, 'observaçao': observaçao, 'destreza': destreza, 'inteligencia': inteligencia, 'carisma': carisma, 'sorte': sorte, 'poder': poder}

dicionarioPersoangens = {}



def criar_personagem(nome, vitalidade, força, observaçao, destreza, inteligencia, carisma, sorte, poder):
    dicionarioPersoangens.update({nome: Personagem(nome, vitalidade, força, observaçao, destreza, inteligencia, carisma, sorte, poder)})


def imprimir_personagem(nome, atributo):
    return(dicionarioPersoangens[nome].atributo[atributo])

def deletar_personagem(nome):
    dicionarioPersoangens.pop(nome)

