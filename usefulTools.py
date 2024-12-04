import random
def getFileExt(filename):
    return filename[filename.index(".")+1:]
def rollDice(num):
    return random.randint(1, num)
class Student:
    def __init__(self, nome, major, gpa, estaEmLiberdadeCondicional):
        self.nome = nome
        self.major = major
        self.gpa = gpa
        self.estaEmLiberdadeCondicional = estaEmLiberdadeCondicional
