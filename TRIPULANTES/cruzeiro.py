class Tripulante:
    def __init__(self, name, age, cod):
        self.name = name
        self.age = age
        self.cod = cod

    def __str__(self) -> str:
        return f"NAME: {self.name},IDADE: {self.age},COD: {self.cod}"

import random

dict = {}

def generate_cod(dict):
    cod = random.randint(1,256)
    if cod in dict.keys():
       return  generate_cod(dict)
    return cod

i = 1000    
while(i != 0):

    print("Digite 1 para inserir um tripilante: ")
    print("Digite 2 cod do tripulhante acessar os seus dados: ")
    print("Digite 0 para sair: ")
    i = int(input("sua opção"))

    if i == 1:
        if len(dict) <= 50:
            name = input("nome do Tripulante")
            age  = input("idade do Tripulante")
            cod = generate_cod(dict)
            print('seu código: ', cod )
            pessoa = Tripulante(name, int(age), cod)
            dict[cod] = pessoa
        else:
            print("Total de tripulantes por viagem atingido")

    if i == 2:
        cod = int(input('digite o cod do tripulante'))
        if cod in dict.keys():
            pessoa = dict[cod]
            print(pessoa)
        else:
            print("cod não existente ! :(")



