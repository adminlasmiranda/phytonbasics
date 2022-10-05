Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Ein Taschenrechner
def menue():
    print('Willkommen bei Ihrem Taschenrechner')
    print('Druecken Sie die ...')
    print('1 um 2 Zahlen zu summieren')
    print('2 um die Differenz von 2 Zahlen zu bestimmen')
    print('3 um das Produkt von 2 Zahlen zu bestimmen')
    print('4 um 2 Zahlen dividieren')
    print('5 um das Programm zu beenden')
while True:
    menue()
    option = input('Geben Sie nun eine der Zahlen ein!: ')
    if option == '1':
        zahl_eins = input('Die erste Zahl, bitte: ')
        zahl_zwei = input('Die zweite Zahl, bitte: ')
        ergebnis_summe = float(zahl_eins) + float(zahl_zwei)
        print('Das Ergebnis ist %s' % ergebnis_summe)
    if option == '2':
        zahl_eins = input('Die erste Zahl, bitte: ')
...         zahl_zwei = input('Die zweite Zahl, bitte: ')
...         ergebnis_differenz = zahl_eins - zahl_zwei
...         print('Das Ergbnis ist %s' % ergebnis_differenz)
...     if option == '3':
...         zahl_eins = input('Die erste Zahl, bitte: ')
...         zahl_zwei = input('Die zweite Zahl, bitte: ')
...         ergebnis_produkt = zahl_eins * zahl_zwei
...         print('Das Ergbnis ist %s' % ergebnis_produkt)
...     if option == '4':
...         zahl_eins = input('Die erste Zahl, bitte: ')
...         zahl_zwei = input('Die zweite Zahl, bitte: ')
...         ergebnis_dividieren = zahl_eins / zahl_zwei
...         print('Das Ergebnis ist %s' % ergebnis_dividieren)
...     if option == '5':
...         print('Auf Wiedersehn')
