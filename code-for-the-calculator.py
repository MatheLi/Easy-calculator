a= "Addition"
b= "Subtraktion"
c= "Muliplikation"
d= "Division"
e= "Potenz"
print("Eingabe 1: Geben Sie eine erste ganze Zahl ein:")
x=int(input())
print("Geben Sie (die passende Zahl) ein ob: addiert (1), multipliziert(2), subtrahiert(3), dividiert(4) oder hochgenommen(5) werden soll:")
p=int(input())
if p==4:
    print("Geben Sie (die passende Zahl) ein ob: das Ergebnis mit Kommastelle (1), die ganze Zahl der division (2), der Rest der division (3)")
    g=int(input())
print("Eingabe 2: Geben Sie eine ganze Zahl ein:")
y=int(input())
if p==1:
    print("Ergebnis der "+a+" ist:")
    print(x+y)
elif p==2:
    print("Ergebnis der " +c+" ist:")
    print(x*y)
elif p==3:
    print("Ergebnis der " +b+" ist:")
    print (x-y)
elif p==4:
    if g==1:
        print("Ergebnis der " +d+" ist:")
        print(x/y)
    elif g==2:
        print("Ergebnis der " +d+" ist:")
        print(x//y)
    elif g==3:
        print("Ergebnis der " +d+" ist:")
        print(x%y)
    else:
        print ("Fehler sind aufgetreten, bitte starten sie das Programm neu")
elif p==5:
    print("Ergebnis der " +e+" ist:")
    print(x**y)
else:
    print ("Fehler sind aufgetreten, bitte starten sie das Programm neu")
    
    
