# https://www.youtube.com/watch?v=rfscVS0vtbw&t=591s
from multiprocessing.managers import Value
from tkinter.font import names

print("hello world")
# Variáveis e tipos de dados
nome = "Bebela"
idade = "22"
print("Oii sou " + nome + " tenho " + idade + " anos")

# string
print("\"quebra linha\"" + "\n OPA!!")
frase = "Ednaldo Pereira"
print(frase.upper() + " " + frase.lower())
#comprimento da string
print(len(frase))
#index
print(frase[0])
print(frase.index("P"))
print(frase.replace("Ednaldo", "Juan"))

# bool
eHomem = False
print(frase.upper().isupper())

# numeros
print((4-42.424242)*2)
numero = 13%5
print(str(numero))
#abs
print(abs(-5))
#pow
print(pow(3,2))
#max e min
print(max(2,9, 1004, 55, 42))
print(min(2,9, 1004, 55, 42))
#arredondar
print(round(3.6))
from math import *
print(floor(3.7))
print(ceil(3.1))
#raiz
print(sqrt(3))

#Conseguir entradas do usuário
#nomeU = input("Digite seu nome: ")
#idadeU = input("Digite sua idade: ")
#print("Olá " + nomeU + "! Sua idade é: " + idadeU)
#num1 = input("num1")
#num2 = input("num2")
#resultado = int(num1) + int(num2)
#resultado = float(num1) + float(num2)
#print(resultado)

#Mad libs
#cor = input("Insira uma cor: ")
#substantivo = input("Insira um substantivo no plural: ")
#celebridade = input("Insira uma celebridade: ")
#print("Rosas são " + cor)
#print(substantivo + " são azuis")
#print("Eu amo " + celebridade)

#listas
amigos = ["sam", "samzinho", "samzinho", "samzinha", "samzento", "samzinho o tormentador"]
print(amigos[4])
amigos[0] = "tuxedosam"
print(amigos[0:5])
#Funções com listas
numerosDaSorte = [43, 5, 55, 555, 5555, 55555]
amigos.extend(numerosDaSorte)
amigos.append("Opa!")
amigos.insert(4, "BMO")
amigos.remove("samzento")
#amigos.clear()
amigos.pop()
print(amigos.index("samzinho"))
print(amigos.count("samzinho"))
#amigos.sort()
numerosDaSorte.sort()
numerosDaSorte.reverse()
print(numerosDaSorte)
amigos2 = amigos.copy()
print(amigos2)

#Tuplas
coordenadas = (4, 5)
#É imutável
print(coordenadas[0])

#Funções
def oi(nome, idade):
    print("Oi " + nome + " sua idade é: " + str(idade))
oi("Beleba", 22)

#return
def aoCubo(num):
    return num*num*num
resultado = aoCubo(4)
print(aoCubo(3))

#If
homi = True
titinha = False
if homi and titinha:
    print("Cabra Macho e titinha")
elif homi and not(titinha):
    print("Cabra Macho e não titinha")
elif homi or titinha:
    print("Cabra Macho ou titinha")
else:
    print("Cabra Fêmea ou normie")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3

print(max_num(1, -1, 5))
#num1 = float((input("Digite um número: ")))
#op = input("Digite um operador: ")
op = "+"
num1 = float(5)
num2 = float(0.5)
#num2 = float((input("Digite mais um número:")))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else :
    print("Operador inválido")

#Dicionários, valor chave em pares
conversaoMeses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Abr" : "Abril",
    "Mai" : "Maio",
    "Jun" : "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro",
}
print(conversaoMeses["Nov"])
print(conversaoMeses.get("Dec", "Não é uma chave válida"))
mes = {
    1 : conversaoMeses["Jan"],
    2 : conversaoMeses["Fev"],
    3 : conversaoMeses["Mar"],
    4 : conversaoMeses["Abr"],
    5 : conversaoMeses["Mai"],
    6 : conversaoMeses["Jun"],
    7 : conversaoMeses["Jul"],
    8 : conversaoMeses["Ago"],
    9 : conversaoMeses["Set"],
    10 : conversaoMeses["Out"],
    11 : conversaoMeses["Nov"],
    12 : conversaoMeses["Dez"],
}
print(mes[1])

#Loops
#While
i = 1
while i <= 10:
    print(i)
    i += 1
print("O loop acabou")

#segredo = "Girafa"
#guess = ""
#guessCount = 0
#guessLimit = 3
#semPalpites = False
#while guess != segredo and not (semPalpites):
#    if guessCount < guessLimit:
#        guess = input("Digite um palpite: ")
#        guessCount += 1
#    else:
#        semPalpites = True
#
#if semPalpites:
#    print("Errouuuu")
#else:
#    print("Acertou!")

#For
amigosos = ["sam", "samzinho", "samzinha"]
for carta in "academia":
    print(carta)
for amigo in amigosos:
    print(amigo)
for index in range(3):
    print(index)
for index in range(3, 10):
    print(index)
for index in range(len(amigosos)):
    print(amigosos[index])

#Função expoente
print(2**3)
def expoente(base, potencia):
    result = 1
    for index in range(potencia):
        result = result * base
    return result
print(expoente(3,2))

#Listas bidimensionais
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(grid[3][0])

#For aninhado
for linha in grid:
    for coluna in linha:
        print(coluna)

#Tradutor
def traduzir(frase):
    traducao = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                traducao = traducao + "G"
            else:
                traducao = traducao + "g"
        else:
            traducao = traducao + letra
    return traducao

#print(traduzir(input("Escreva uma Frase: ")))
'''
comentário!!!
'''
#Detecção de erros e exceç
#invalid literal for int() with base 10: -> colocando valor de string em um numero
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Entrada Inválida")

# Leitura de Arquivos
#open("employees.txt", "r+")
#open("employees.txt", "w")
#open("employees.txt", "a")
employeeFile = open("employees.txt", "r")
print(employeeFile.readable())
#print(employeeFile.read())
#print(employeeFile.readline()) #lê apenas primeira linha
for employee in employeeFile.readlines():
    print(employee)
#print(employeeFile.readlines()[1])
employeeFile.close()

# Escrever e anexar arquivos
employeeFile = open("employees.txt", "a")
employeeFile = open("employees.txt1", "a")
employeeFile.write("\nKelly - Customer Service")

#Módulos e Pip
import usefulTools
print(usefulTools.rollDice(6))
#Lista de módulos python
#pip install python-docx

#Classes e Objetos
from usefulTools import Student
student1 = Student("Jim", "Business", "3.1", False)
print(student1.gpa

#heranca from Chef import Chef class ChineseChef(Chef)