nome ="gabriela"
idade = "16"
data_de_nascimento = "05.10.2008"
print("meu nome é", nome, "tenho", idade, "de idade, e nasci em", data_de_nascimento)

# tipos de variaveis

nome = "Gabi"
idade = 16
altura = 1.62
ativo = True

print( "o tipo de variavel nome é:",type(nome))
print( "o tipo de variavel idade é:",type(idade))
print("o tipo de variavel altura é:",type(altura))
print("o tipo de variavel ativo é:",type(ativo))




#operadores

print(30*'-' ,'operadores',30*'-')


num1 = 10
num2 = 10

soma = num1 + num2
divi = num1 / num2 # divisao cumum
divisao_inteira = num1 * num2 # divisao inteira
mult = num1 - num2
expo = num1 ** num2 
sub = num1 - num2
resto = num1 %2

print("resultado da soma", num1, "+", num2, "é", soma)
print("resultado da divisao", num1, "/", num2, "é",divi)
print("resultado da divisao inteira é:" ,divisao_inteira)
print("resultado da multiplicaçao", num1, "x", num2, "é:", mult)
print("resultado do expoente é:", expo)
print("resultado da subtracao", num1,"-", num2, "e", sub)
print("resultado do resto de", num1, "é:" ,resto)

print()
print(30*'-','operadores de comparaçao' ,30*'-')

#operadores de comparaçao
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("ano atual:",ano)
ano += 1
print("ano acrecido de +1:",ano)
ano -= 1
print("ano descrecido de -1:",ano)

# O perações lógicos
# AND, OR, NOT

print ()
print(30*'-','calculadora',30*'-')

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

soma = numero1 + numero2
divi = numero1 / numero2
mult = numero1 * numero2
sub = numero1 - numero2

print('resultado da soma',numero1,"+", numero2, "é", soma)

ano_nascimento = input("digita seu ano de nascimento")
print(type(ano_nascimento))
#convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

saudacao = input('digite seu nome: ')
cpf = input('digite seu cpf: ')
telefone = input("digite seu telefone: ")

print(20*'-','dados pessoais' ,20*'-')
print('nome:', saudacao)
print(50*'-')
      