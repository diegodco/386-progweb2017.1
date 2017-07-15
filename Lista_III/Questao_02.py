'''
 Diêgo C. Oliveira
 Tec. em Informática | IFPI
 Programação para Web | Ritomar Torquato
 Turma 386, Periodo 2017.1

2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
'''
nome_usuario = input("Nome de Usuário: ")
senha_usuario = input("Senha: ")
while nome_usuario == senha_usuario:
    print("\nA senha não pode ser igual ao nome de usuário!")
    senha_usuario = input("Digite a senha novamente: ")
print("\nOperação realizada com sucesso!")