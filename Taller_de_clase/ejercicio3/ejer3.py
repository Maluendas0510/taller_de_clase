# ejercicio 3

from traceback import print_tb


print("------------------------")
print("---serie finonacci------")
print("------------------------")

#input
a=0
b=1
n=0
#processing
while(n<1000):
    n=a+b
    print(n , end=" ")
    a=b
    b=n
    
    