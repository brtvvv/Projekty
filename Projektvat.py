#Menu główne programu
from cleaner import clean


while True:
    clean
    print("Kalkulator podatku VAT")
    print()
    print("Made by: Bartosz Ołka")
    
    print("1) Obliczanie ceny Netto")
    print()
    print("2) Obliczanie ceny Brutto")
    print()
    print("3) Wyjscie")

    wybor = input("Podaj wybor: ")

#Obliczanie ceny netto
    if wybor == "1":
        print()
        print("Obliczanie ceny Netto")
        Vat = float(input("Podaj wartość VAT: "))
        CenaBrutto = int(input("Podaj cene brutto: "))
        CenaNetto = CenaBrutto / Vat
        print(CenaNetto)
        kontynuacja = input("Jezeli chcesz wrocic do menu nacisnij enter")
        if kontynuacja == '':
            continue

#obliczanie ceny brutto
    if wybor == "2":
        print()
        print("Obliczanie ceny brutto")
        Vat = float(input("Podaj wartość VAT: "))
        CenaNetto = int(input("Podaj cene netto: "))
        CenaBrutto = CenaNetto * Vat
        print(CenaBrutto)
        kontynuacja = input("Jeżeli chcesz wrocic do menu nacisnij enter")
        if kontynuacja == "":
            continue
#wyjscie
    if wybor == "3":
        break

    else:
        print()
        unknown = input("Niewlasciwa komenda, aby powrocic do menu nacisnij przycisk enter: ")
        if unknown == "":
            continue
        

