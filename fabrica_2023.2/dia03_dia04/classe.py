from abc import ABC, abstractclassmethod
# Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope LocalMachine
# Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
# .\venv\Script\activate
# pip install django
# pip install djangorestframework
# django-admin startproject agenda 
# cria arquivo .gitignore e coloca lá
# venv
# *.sqlite3
# __pycache__

class IAnimal(ABC):
    
    #@abstractmethod
    def falar(self):
        """defina na classe filha"""
    
    #@abstractmethod
    def andar(self):
        """defina na classe filha"""
        
class Cachorro(IAnimal):
    def falar(self):
        print("AuAu")
    
    def andar(self):
        print("Ando com 4 patas")
        
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__humano = True
    
    def fala_pessoa(self):
        print("Falando")
    def mostra_nome(self):
        print(self.nome)
        
        
pingo = Cachorro()
pingo.falar

humano = Pessoa("Bruno", 20)

humano.fala_pessoa()
humano.mostra_nome()