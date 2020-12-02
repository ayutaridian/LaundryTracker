# Validasi input sesuai tipe data tertentu

def inputInt(message):
    while True:
        try:
            userInput = int(input(message + ": "))       
        except ValueError:
            print(message + " harus berisi integer.")
            continue
        else:
            return userInput 
            #break

def inputFloat(message):
    while True:
        try:
            userInput = float(input(message + ": "))       
        except ValueError:
            print(message + " harus berisi float.")
            continue
        else:
            return userInput 
            #break

def inputString(message):
    while True:
        try:
            userInput = input(message + ": ")      
        except ValueError:
            print(message + " harus berisi string.")
            continue
        else:
            return userInput 
            #break

def inputList(length):
    userInput = []
    for _ in range (length):
        userInput.append(input())
    return userInput