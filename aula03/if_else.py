
import this
# FIXME - concatenação com +

nome = "Gabriela"
idade = 16
altura = 1.62

# saida de dados
print("ola, meu nome é" "+ nome +","tenho" + str(idade) + "anos de idade")

#FIXME - concatenação com ,
print ("ola, meu nome é," "nome", " tenho" , idade, " anos de idade")

#FIXME - concatenação com format
print("ola, meu nome é{}, tenho {} anos de idade" .format(nome,idade))

#FIXME - concatenação com f-string
print(f"ola, meu nome é (nome) e tenho (idade+1) anos de idade")


# eliminando quebra de limite
print("o sabio sabia", end=" ")
print("que o sabiá sabia assobiar.")


valor = 1.23456789

# exibindo o valor com duas casas depois da virgula
print(f"{valor:,.2f}")

print(30*"=")
peso = input('digite seu peso:')
peso = float(peso)
print(f"{peso:.2f}")

nome = input('digite seu nome')
idade = int(input('digite sua idade: '))

print('antes do if')
if idade >= 18:
    print("voce é maior de idade! ")
    print('voce esta dentro do bloco if')
else:
    print('voce é menor de idade!')
    print("voce esta dentro do bloco ELSE")
print("voce esta fora da estrutura condicional if else")

num1 = 10
if num1 %2 == 0:
 print('numero par')
else:
   print('numero impar')

   print(40*'-','BOLETIM ESCOLAR',40*'-')
   nome_aluno = input('digite o nome do aluno')
   nota1 = float(input('digita a primeira nota: '))
   nota2 = float(input('digita a segunda nota: '))
   nota3 = float(input('digita a terceira nota: '))
   nota4 = float(input('digita a quarta nota: '))

   media = (nota1+nota2+nota3+nota4)/4
   
   # >= 7: aprovado
   # >= 5: recuperaçao
   # reprovado

   if media >=7:
     print(f'{nome_aluno}!!!Aluno aprovado!')
     print(f'Nota 1: {nota1}| Nota 2: {nota2}')
     print(f'Nota 3: {nota3}| Nota 4: {nota4}')
     print(20*'=')
     print(f'Média: {media}')

   elif media >= 5:
     print(f'{nome_aluno}!!!Aluno em recuperação!')
     print(f'Nota 1: {nota1}| Nota 2: {nota2}')
     print(f'Nota 3: {nota3}| Nota 4: {nota4}')
     print(20*'=')
     print(f'Média: {media}')

   else:
    print(f'{nome_aluno}!!!Aluno reprovado!')
    print(f'Nota 1: {nota1}| Nota 2: {nota2}')
    print(f'Nota 3: {nota3}| Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')

