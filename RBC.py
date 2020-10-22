# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:21:03 2020

@authors: Jonath, Andriy, Matheus
"""

from tkinter import *

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

def calculateSimilarity():
    textCars.delete(1.0,END)
    
    entry = []
    entry.append(buying.get())
    entry.append(mant.get())
    entry.append(doors.get())
    entry.append(persons.get())
    entry.append(lugBoot.get())
    entry.append(safety.get())
    
    arrayEntry = convertData(entry)
    
    weight = []
    weight.append(float(buyingWeight.get()))
    weight.append(float(mantWeight.get()))
    weight.append(float(doorsWeight.get()))
    weight.append(float(personsWeight.get()))
    weight.append(float(lugBootWeight.get()))
    weight.append(float(safetyWeight.get()))
    
    buyingTable = [[1, 0.66, 0.33, 0],
              [0.66, 1, 0.66, 0.33],
              [0.33, 0.66, 1, 0.66],
              [0, 0.33, 0.66, 1]]
    
    maintenanceTable = [[1, 0.66, 0.33, 0],
                  [0.66, 1, 0.66, 0.33],
                  [0.33, 0.66, 1, 0.66],
                  [0, 0.33, 0.66, 1]]
    
    doorsTable = [[1, 0.66, 0.33, 0],
             [0.66, 1, 0.66, 0.33],
             [0.33, 0.66, 1, 0.66],
             [0, 0.33, 0.66, 1]]
    
    personsTable = [[1, 0.33, 0],
               [0.33, 1, 0.66],
               [0, 0.66, 1]]
    
    lugBootTable = [[1, 0.5, 0],
               [0.5, 1, 0.5],
               [0, 0.5, 1]]
    
    safetyTable = [[1, 0.5, 0],
              [0.5, 1, 0.5],
              [0, 0.5, 1]]
    
    attributes = [buyingTable, maintenanceTable, doorsTable, personsTable, lugBootTable, safetyTable]
    
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
    
    #print('\nClasse carro de entrada: ' + carList[0].classi)
    #print('\nTop 3 carros com maior similaridade:')
    #for i in range(3):
    #    print(carList[i].printCar())
    
    labelClassResult.config(text=carList[0].classi)
    
    i=1
    for item in carList:
        textCars.insert(END, str(i)+") "+item.printCar()+"\n")
        i+=1
        
    #f = open("carResult.data", "w")
    #for item in carList:
    #    f.write("%s\n" % item.printCar())
    #f.close()
    
if __name__ == '__main__':
    root = Tk()
    root.title("RBC")
    
    root.geometry("485x600")
    
    labelAttributes = Label(root, text="Atributos").grid(row=0, column=0)
    labelBuying = Label(root, text="Preço de compra").grid(row=1, column=0)
    labelMant = Label(root, text="Preço de manutenção").grid(row=2, column=0)
    labelDoors = Label(root, text="Quantidade de portas").grid(row=3, column=0)
    labelPersons = Label(root, text="Capacidade de pessoas").grid(row=4, column=0)
    labelLugBoot = Label(root, text="Capacidade de bagagem").grid(row=5, column=0)
    labelSafety = Label(root, text="Nível de segurança").grid(row=6, column=0)
    
    labelValues = Label(root, text="Valores").grid(row=0, column=1)
    
    buying = StringVar(root)
    buying.set("low")
    optionBuying = OptionMenu(root, buying, "low", "med", "high", "vhigh")
    optionBuying.config(width=5)
    optionBuying.grid(row=1, column=1)
    
    mant = StringVar(root)
    mant.set("low")
    optionMant = OptionMenu(root, mant, "low", "med", "high", "vhigh")
    optionMant.config(width=5)
    optionMant.grid(row=2, column=1)
    
    doors = StringVar(root)
    doors.set("2")
    optionDoors = OptionMenu(root, doors, "2", "3", "4", "5more")
    optionDoors.config(width=5)
    optionDoors.grid(row=3, column=1)
    
    persons = StringVar(root)
    persons.set("2")
    optionPersons = OptionMenu(root, persons, "2", "4", "more")
    optionPersons.config(width=5)
    optionPersons.grid(row=4, column=1)
    
    lugBoot = StringVar(root)
    lugBoot.set("small")
    optionLugBoot = OptionMenu(root, lugBoot, "small", "med", "big")
    optionLugBoot.config(width=5)
    optionLugBoot.grid(row=5, column=1)
    
    safety = StringVar(root)
    safety.set("low")
    optionSafety = OptionMenu(root, safety, "low", "med", "high")
    optionSafety.config(width=5)
    optionSafety.grid(row=6, column=1)
    
    labelWeights = Label(root, text="Pesos").grid(row=0, column=2)
    
    buyingWeight = Entry(root, width=5)
    buyingWeight.insert(0, "1")
    buyingWeight.grid(row=1, column=2)
    
    mantWeight = Entry(root, width=5)
    mantWeight.insert(0, "0.2")
    mantWeight.grid(row=2, column=2)
    
    doorsWeight = Entry(root, width=5)
    doorsWeight.insert(0, "0.5")
    doorsWeight.grid(row=3, column=2)
    
    personsWeight = Entry(root, width=5)
    personsWeight.insert(0, "1")
    personsWeight.grid(row=4, column=2)
    
    lugBootWeight = Entry(root, width=5)
    lugBootWeight.insert(0, "0.75")
    lugBootWeight.grid(row=5, column=2)
    
    safetyWeight = Entry(root, width=5)
    safetyWeight.insert(0, "1")
    safetyWeight.grid(row=6, column=2)
    
    btn = Button(root, text="Calcular", command=calculateSimilarity, bg="lightgreen").grid(row=8, column=1)
    
    labelClassResultText = Label(root, text="Classe carro de entrada: ").grid(row=9, column=0, sticky=W)
    
    labelClassResult = Label(root, bg="red")
    labelClassResult.grid(row=9, column=0, sticky=E)
    
    labelText = Label(root, text="Carros com maior similaridade:").grid(row=10, column=0, sticky=W)
    
    textCars = Text(root, width=60)
    textCars.grid(row=11, columnspan=3)
    
    root.mainloop()
    