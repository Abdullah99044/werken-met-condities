print("Is de kaas geel?")
a = input("Ja/Nee")
if a ==  "ja":
    print("Zitten er gaten in?")
    b = input("ja/nee")
    if b == "ja":
        print("Is de kaas belachelijk duur")
        c = input("ja/nee")
        if c == "ja":
            print("Emmenthaler")
        else :
                 print("Leerdammer")
    else:
       if b == "nee":
           print("Is de kaas hard als steen?")
           d = input("ja/nee")
           if d == "ja":
               print("Parmigiano Reggiano")

           else:
                if d == "nee":
                    print("Gaudse kaas")
else:
    if a == "nee":
        print("Heeft de kaas blauwe schimmels?")
        e = input("ja/nee")
        if e == "ja":
            print("Heeft de kaas een korst?")
            f = input("ja/nee")
            if f == "ja":
                print("Bleu de Rochbaron")
            else:
                if f == "nee":
                    print("Foume D'Ambert")  
        else:
            if e == "nee":
                print("Heeft de kaas een korst?")
                g = input("ja/nee")
                if g == "ja":
                    print("Camembert")
                else:
                    if g == "nee":
                        print("Mozzarella")    
