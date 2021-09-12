
#introductie
print("******************************************************")
print("*    Sollicitatieformulier  voor Circusdirecteur     *")
print("******************************************************")
print("Om in aanmerking te komen voor een sollicitatiegesprek")
print("moet je als kandidaat eerst de vragenlijst beantwoorden")
print("           via dit Sollicitatieformulier              ")
print("******************************************************")

#vragenlijst
print("Wat is uw naam?")
naam = input("Uw naam?")

print("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?")
a = int(input("Hoveel?"))
min = 4
if a > min:
    print("Bent u bezit van een Diploma MBO-4 ondernemen?")
    b = input("ja/nee?")
    if b == "ja":
        print("Heeft u een geldig Vrachtwagen rijbewijs?")
        c = input("ja/nee?")
        if c == "ja":
            print("Heeft u een hoge hoed?")
            d = input("ja/nee?")
            if d == "ja":
                print("Bent u een man en heeft u Snor breder dan 10 cm of een vrouw en draagt u rood krulhaar lanhet dan 20 cm ?")
                e = input("ja/nee?")
                if e == "ja":
                    print("Bent u lanhet dan 150 cm?")
                    f = input("ja/nee?")
                    if f == "ja":
                        print("Weegt  u zwaarder dan 90kg")
                        g = input("ja/nee?")
                        if g == "ja":
                            print("Heeft u Certificaat “Overleven met gevaarlijk personeel?")
                            h = input("ja/nee?")
                            if h == "ja":
                                print("Kan u dansen?")
                                dansen = input("ja/nee?")
                                print("Heb u een ongeluk gehad? en hoe was dat?")
                                ongeluk = input("ja/nee?")
                                print("Heb u een mooie stem?")
                                stem = input("ja/nee")
                                print("waarom heb u voor deze baan gekozen?")
                                baan = input("vetrel")
                                print("gefeliciteerd! u komt in aanmerking voor een sollicitatiegesprek, stuur uw cv.")
                            else:
                                if h == "nee":
                                    print("beste" , naam )
                                    print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                        else:
                            if g == "nee":
                                print("beste" , naam )
                                print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                    else:
                        if f == "nee":
                            print("beste" , naam )
                            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                    
                else:
                    if e == "nee":
                        print("beste" , naam )
                        print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
            else:
                if d == "nee":
                    print("beste" , naam )
                    print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
        else:
            if c == "nee":
                  print("beste" , naam )
                  print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")  
    else:
        if b == "nee":
            print("beste" , naam )
            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")
else :
    if a < min:
        print("Hoeveel jaar praktijkervaring heeft u met jongleren?")
        i = int(input("Hoveel?"))
        minB = 5 
        if i > 5:
                print("Bent u bezit van een Diploma MBO-4 ondernemen?")
                b = input("ja/nee?")
                if b == "ja":
                    print("Heeft u een geldig Vrachtwagen rijbewijs?")
                    c = input("ja/nee?")
                    if c == "ja":
                        print("Heeft u een hoge hoed?")
                        d = input("ja/nee?")
                        if d == "ja":
                            print("Bent u een man en heeft u Snor breder dan 10 cm of een vrouw en draagt u rood krulhaar lanhet dan 20 cm ?")
                            e = input("ja/nee?")
                            if e == "ja":
                                print("Bent u lanhet dan 150 cm?")
                                f = input("ja/nee?")
                                if f == "ja":
                                    print("Weegt  u zwaarder dan 90kg")
                                    g = input("ja/nee?")
                                    if g == "ja":
                                        print("Heeft u Certificaat “Overleven met gevaarlijk personeel?")
                                        h = input("ja/nee?")
                                        if h == "ja":
                                            print("Kan u dansen?")
                                            dansen = input("ja/nee?")
                                            print("Heb u een ongeluk gehad? en hoe was dat?")
                                            ongeluk = input("ja/nee?")
                                            print("Heb u een mooie stem?")
                                            stem = input("ja/nee")
                                            print("waarom heb u voor deze baan gekozen?")
                                            baan = input("vetrel")
                                            print("gefeliciteerd! u komt in aanmerking voor een sollicitatiegesprek, stuur uw cv.")
                                        else:
                                            if h == "nee":
                                                print("beste" , naam )
                                                print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                    else:
                                        if g == "nee":
                                            print("beste" , naam )
                                            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                else:
                                    if f == "nee":
                                        print("beste" , naam )
                                        print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                
                            else:
                                if e == "nee":
                                    print("beste" , naam )
                                    print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                        else:
                            if d == "nee":
                                print("beste" , naam )
                                print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                    else:
                        if c == "nee":
                            print("beste" , naam )
                            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")  
                else:
                    if b == "nee":
                        print("beste" , naam )
                        print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")
        else:
            if i < 5:
                print("Hoeveel jaar praktijkervaring heeft u met acrobatiek?")
                mind = 3
                z = int(input("hoveel?"))
                if mind < z:
                    print("Bent u bezit van een Diploma MBO-4 ondernemen?")
                    b = input("ja/nee?")
                    if b == "ja":
                        print("Heeft u een geldig Vrachtwagen rijbewijs?")
                        c = input("ja/nee?")
                        if c == "ja":
                            print("Heeft u een hoge hoed?")
                            d = input("ja/nee?")
                            if d == "ja":
                                print("Bent u een man en heeft u Snor breder dan 10 cm of een vrouw en draagt u rood krulhaar lanhet dan 20 cm ?")
                                e = input("ja/nee?")
                                if e == "ja":
                                    print("Bent u lanhet dan 150 cm?")
                                    f = input("ja/nee?")
                                    if f == "ja":
                                        print("Weegt  u zwaarder dan 90kg")
                                        g = input("ja/nee?")
                                        if g == "ja":
                                            print("Heeft u Certificaat “Overleven met gevaarlijk personeel?")
                                            h = input("ja/nee?")
                                            if h == "ja":
                                                print("Kan u dansen?")
                                                dansen = input("ja/nee?")
                                                print("Heb u een ongeluk gehad? en hoe was dat?")
                                                ongeluk = input("ja/nee?")
                                                print("Heb u een mooie stem?")
                                                stem = input("ja/nee")
                                                print("waarom heb u voor deze baan gekozen?")
                                                baan = input("vetrel")
                                                print("gefeliciteerd! u komt in aanmerking voor een sollicitatiegesprek, stuur uw cv.")
                                            else:
                                                if h == "nee":
                                                    print("beste" , naam )
                                                    print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                        else:
                                            if g == "nee":
                                                print("beste" , naam )
                                                print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                    else:
                                        if f == "nee":
                                            print("beste" , naam )
                                            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                                    
                                else:
                                    if e == "nee":
                                        print("beste" , naam )
                                        print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                            else:
                                if d == "nee":
                                    print("beste" , naam )
                                    print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!") 
                        else:
                            if c == "nee":
                                print("beste" , naam )
                                print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")  
                    else:
                        if b == "nee":
                            print("beste" , naam )
                            print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")
                else:
                    if z > mind:

                        print("beste" , naam )
                        print("U voldoet niet aan onze strenge eisen voor functie van Circusdirecteur , het spijt ons!")
                        