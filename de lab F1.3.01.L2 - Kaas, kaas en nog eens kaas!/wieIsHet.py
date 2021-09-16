while True:    
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
            elif c == "nee":
                    print("Leerdammer")
        elif  b == "nee":
                print("Is de kaas hard als steen?")
                d = input("ja/nee")
                if d == "ja":
                    print("Parmigiano Reggiano")
                elif d == "nee":
                    print("Gaudse kaas")
    elif a == "nee":
            print("Heeft de kaas blauwe schimmels?")
            e = input("ja/nee")
            if e == "ja":
                print("Heeft de kaas een korst?")
                f = input("ja/nee")
                if f == "ja":
                    print("Bleu de Rochbaron")
                elif f == "nee":
                        print("Foume D'Ambert")  
            elif e == "nee":
                    print("Heeft de kaas een korst?")
                    g = input("ja/nee")
                    if g == "ja":
                        print("Camembert")
                    elif g == "nee":
                            print("Mozzarella")            