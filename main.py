nome = input('Digite seu nome: ')
sobrenome = input('Digite seu Sobre nome: ')
cidade = input('Qual sua cidade: ')
profissao = input('Qual sua profissao: ')
ano_nascimento = input('Em qual ano voce nasceu:')
idade = 2022 - int(ano_nascimento)

senha = input('Digite uma Senha: sem caracteres e sem letras: somente numeros: ')
senha2 = input('Confirme sua senha: ')

texto = f' o {nome} {sobrenome} mora na cidade de: {cidade} e um execelente [{profissao}] e tem {idade} de idade'


while senha != senha2:
    print('Erro! senha digitada errada, confirme a senha e digite novamente')

    senha = input('Digite uma Senha: sem caracteres e sem letras: somente numeros: ')
    senha2 = input('Confirme sua senha: ')

if senha == senha2:
    print('Senha correta parabenz: cadastro feito com sucesso!')
    print(texto)



"""nome = input('Digite seu nome: ')
with open('arquivo.json', 'at+', encoding='utf8') as file:
    file.write(f"{nome}\n")"""
git add
