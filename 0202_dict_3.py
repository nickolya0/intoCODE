dict = {                                # initialisen wir ein Dictionary. key-value.
    'Name':         'Mykola',
    # 'Nachname':     'Zitser',
    'Alter':        '36', # -
    # 'Grosse':       '183',
    'Wohnort':      [] # -

}
WohnortList = ['Bismarkstr', 2, 30100]                      # initialisieren wir eine Liste
WohnortList1 = ['Bahnhof', 6, 30700]


def dictManipulieren(dict):               # definieren eine Funktion mit übergabene parameter

    dict['Wohnort'] = [WohnortList, WohnortList1]

dictManipulieren(dict)
print(dict)
