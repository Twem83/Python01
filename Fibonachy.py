# funcion factorial recursiva  y serie fibonacci
def fact(i):
    if i==0:
        return 1
    else :
        return i*fact(i-1)
a,b,i=0,1,1
print("Ingrese Numero :")
F=input()
while i<=int(F):
    b,a=a+b,b
    print(i,"-->",b,"  Fact(",i,")=",fact(i))
    i=i+12