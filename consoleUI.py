from main import *
import main

def testMenuUI():
    print('''
#============================================================================================#\n
Maak een keuze voor het testen
1: Stel regel op.
2: Pas regel toe.
3: Commit naar DB
10: done
#============================================================================================#\n
''')

def autoLoginUpdateUI():
    print('''
#============================================================================================#\n
Maak de volgende keuzes om de autologin te updaten met nieuwe informatie.
1: gebruikersnaam
2: wachtwoord
3: Done
#============================================================================================#\n
''')

def regelmakerUIInformatie():
    print(''''
#============================================================================================#\n
1: Haal informatie op over aanwezige tabellen.
2: Haal tabel informatie op.
3: Bouw regel.
4: Stop
#============================================================================================#\n
''')

def regelMakerUI(cursor, db):
    flag = True
    while flag:
        regelmakerUIInformatie()
        check = True
        while check:
            invoer = input()
            if invoer == '1':
                print(main.pakTables(cursor))
                check = False
            elif invoer == '2':
                print(2)
                check = False
            elif invoer == '3':
                regel = main.regelMaker(cursor, db)
                check = False
            elif invoer == '4':
                print("Stopping")
                flag = False
                check = False
            else:
                print('Geen geldige input')

def regelmakerUIBouwRegel():
    print('''
#============================================================================================#\n
1: 
2: 
#============================================================================================#\n
''')

def testMenu():
    testMenuUI()
    flag = True
    loginInfo = main.autoLogin()
    db, cursor = mysqlConnectie(loginInfo)

    while flag:
        keuze = input()
        if keuze == '1':
            regels = main.regelMaker(cursor, db)
        elif keuze == '2':
            regelMakerUI(cursor, db)
        elif keuze == '3':
            print("3")
        elif keuze == '10':
            flag = False

    mysqlSluit(db, cursor)