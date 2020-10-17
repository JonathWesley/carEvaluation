# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:21:03 2020

@author: Jonath, Andriy, Matheus
"""

class Car:
    def __init__(self, buying, mant, doors, persons, lugBoot, safety, classi, similarity):
        self.buying = buying
        self.mant = mant
        self.doors = doors
        self.persons = persons
        self.lugBoot = lugBoot
        self.safety = safety
        self.classi = classi
        self.similarity = similarity
        
    def printCar(self):
        return str(self.buying)+','+str(self.mant)+','+str(self.doors)+','+str(self.persons)+','+str(self.lugBoot)+','+str(self.safety)+','+str(self.classi)+','+str(self.similarity)

def convertBM(string):
    if string == 'vhigh':
        return 3
    elif string == 'high':
        return 2
    elif string == 'med':
        return 1
    else:
        return 0
    
def convertDoors(string):
    if string == '2':
        return 0
    elif string == '3':
        return 1
    elif string == '4':
        return 2
    else:
        return 3
    
def convertPersons(string):
    if string == '2':
        return 0
    elif string == '4':
        return 1
    else:
        return 2
    
def convertLugBoot(string):
    if string == 'small':
        return 0
    elif string == 'med':
        return 1
    else:
        return 2

def convertSafety(string):
    if string == 'low':
        return 0
    elif string == 'med':
        return 1
    else:
        return 2

def convertData(data):
    arrayData = []
    arrayData.append(convertBM(data[0]))
    arrayData.append(convertBM(data[1]))
    arrayData.append(convertDoors(data[2]))
    arrayData.append(convertPersons(data[3]))
    arrayData.append(convertLugBoot(data[4]))
    arrayData.append(convertSafety(data[5]))
    
    return arrayData
    
if __name__ == '__main__':
    buyMantSet = {'low', 'med', 'high', 'vhigh'}
    doorSet = {'2', '3', '4', '5more'}
    personSet = {'2', '4', 'more'}
    lugBootSet = {'small', 'med', 'big'}
    safetySet = {'low', 'med', 'high'}
    alterWeight = {'s', 'n'}
    
    entryBuying = input("Insira o preço de compra (low, med, high, vhigh): ")
    while entryBuying not in buyMantSet:
        entryBuying = input("Insira o preço de compra (low, med, high, vhigh): ")
        
    entryMant = input("Insira o preço de manutenção (low, med, high, vhigh): ")
    while entryMant not in buyMantSet:
        entryMant = input("Insira o preço de manutenção (low, med, high, vhigh): ")
        
    entryDoor = input("Insira a quantidade de portas (2, 3, 4, 5more): ")
    while entryDoor not in doorSet:
        entryDoor = input("Insira a quantidade de portas (2, 3, 4, 5more): ")
        
    entryPerson = input("Insira a capacidade de pessoas (2, 4, more): ")
    while entryPerson not in personSet:
        entryPerson = input("Insira a capacidade de pessoas (2, 4, more): ")
        
    entryLugBoot = input("Insira a capacidade de bagagem (small, med, big): ")
    while entryLugBoot not in lugBootSet:
        entryLugBoot = input("Insira a capacidade de bagagem (small, med, big): ")
        
    entrySafety = input("Insira a segurança (low, med, high): ")
    while entrySafety not in safetySet:
        entrySafety = input("Insira a segurança (low, med, high): ")
    
    entry = []
    entry.append(entryBuying)
    entry.append(entryMant)
    entry.append(entryDoor)
    entry.append(entryPerson)
    entry.append(entryLugBoot)
    entry.append(entrySafety)
    
    weight = [1, 0.2, 0.5, 1, 0.75, 1]
    
    entryWeight = input("Deseja alterar os pesos? (s/n): ")
    while entryWeight not in alterWeight:
        entryWeight = input("Deseja alterar os pesos? (s/n): ")
        
    if entryWeight == 's':
        while True:
            try:
                buyingWeight = float(input("Peso do valor de compra ("+str(weight[0])+"): "))
            except ValueError:
                pass
            else:
                break
            
        while True:
            try:
                mantWeight = float(input("Peso do valor de compra ("+str(weight[1])+"): "))
            except ValueError:
                pass
            else:
                break
         
        while True:
            try:
                doorWeight = float(input("Peso do valor de compra ("+str(weight[2])+"): "))
            except ValueError:
                pass
            else:
                break
         
        while True:
            try:
                personWeight = float(input("Peso do valor de compra ("+str(weight[3])+"): "))
            except ValueError:
                pass
            else:
                break
            
        while True:
            try:
                lugBootWeight = float(input("Peso do valor de compra ("+str(weight[4])+"): "))
            except ValueError:
                pass
            else:
                break
            
        while True:
            try:
                safetyWeight = float(input("Peso do valor de compra ("+str(weight[5])+"): "))
            except ValueError:
                pass
            else:
                break
        
        weight = [buyingWeight, mantWeight, doorWeight, personWeight, lugBootWeight, safetyWeight]
    
    arrayEntry = convertData(entry)
    
    buying = [[1, 0.66, 0.33, 0],
              [0.66, 1, 0.66, 0.33],
              [0.33, 0.66, 1, 0.66],
              [0, 0.33, 0.66, 1]]
    
    maintenance = [[1, 0.66, 0.33, 0],
                  [0.66, 1, 0.66, 0.33],
                  [0.33, 0.66, 1, 0.66],
                  [0, 0.33, 0.66, 1]]
    
    doors = [[1, 0.66, 0.33, 0],
             [0.66, 1, 0.66, 0.33],
             [0.33, 0.66, 1, 0.66],
             [0, 0.33, 0.66, 1]]
    
    persons = [[1, 0.33, 0],
               [0.33, 1, 0.66],
               [0, 0.66, 1]]
    
    lugBoot = [[1, 0.5, 0],
               [0.5, 1, 0.5],
               [0, 0.5, 1]]
    
    safety = [[1, 0.5, 0],
              [0.5, 1, 0.5],
              [0, 0.5, 1]]
    
    attributes = [buying, maintenance, doors, persons, lugBoot, safety]
    
    carList = []
    
    f = open("car.data", "r")
    for line in f:
        line = line.strip('\n')
        data = line.split(',')
        arrayData = convertData(data)
        
        num = 0
        for i in range(len(entry)):
            num += weight[i] * attributes[i][arrayEntry[i]][arrayData[i]]
        similarity = num / sum(weight, 0)
        
        carList.append(Car(data[0], data[1], data[2], data[3], data[4], data[5], data[6], similarity))
    f.close()
    
    carList.sort(key=lambda x: x.similarity, reverse=True)
    
    print('\nClasse carro de entrada: ' + carList[0].classi)
    print('\nTop 3 carros com maior similaridade:')
    for i in range(3):
        print(carList[i].printCar())
        
    f = open("carResult.data", "w")
    for item in carList:
        f.write("%s\n" % item.printCar())
    f.close()

    