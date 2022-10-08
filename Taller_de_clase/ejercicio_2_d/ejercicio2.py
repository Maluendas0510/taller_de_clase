# Ejercicio 2

print("---------------------")
print("--- numero inverso---")
print("---------------------")

#input
n=int(input("Digite el valor del numero :"))
k=0
m=n
# processing
while(n!=0):
    r=(n%10)
    k=(k*10)+r   
    n=n//10
    
print("El valor dijitado es " + str(m) +" y su numero inverso es " + str (k))    