'''On définit le global direct dans la fonction pas
besoin de la redéfinir dans les autres fonctions'''

def procedure(a,b):
    global total
    total = a+b

def multiplication(x):
    result = x*total
    return result

procedure(2,2)
print(multiplication(2))

def factorial(n):
    total = 1
    facto = 1
    while facto<n:
        facto+=1
        total*=facto
    return total

print(factorial(2))

print(factorial(4))

