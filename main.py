from dataIN import *
from dataUIT import *
from consoleUI import *
import json
import mysql

# def autoLoginUpdate():
#     try:
#         with open('login.txt')
#
# def autoLoginUpdateMenu():
#     klaar = True
#     while klaar:
#         autoLoginUpdateUI()
#         gekozen = True
#         while gekozen:
#             keuze = input()
#             if keuze == "1" or "2" or "3":
#                 print("Hoi")
#                 gekozen = False

def mysqlConnectie(loginInfo):
    """"
    Verbinding met de gekozen mysql database.
    :arg gebruiker ; Gebruikersnaam
    :arg wachtwoord ; wachtwoord behorend bij gebruikersnaam
    :arg dbNaam ; de naam van de database waarin gezoekt moet worden.
    :arg host ; de link naar de server. Voor localhost gebruik ("localhost")
    """
    db = mysql.connector.connect(host=loginInfo["host"], user=loginInfo["gebruiker"], password=loginInfo["wachtwoord"], database=loginInfo["dbNaam"])
    cursor = db.cursor()

    return db, cursor

def mysqlSluit(db, cursor):
    cursor.close()
    db.commit()
    db.close()

def autoLogin():
    try:
        open('login.txt')
    except FileNotFoundError:
        devOpties = {'gebruiker': "root",
                     'wachtwoord': "",
                     'dbNaam': "test",
                     'host': "localhost"}
        with open('login.txt', 'w') as file:
            file.write(json.dumps(devOpties))
            file.close()

    with open('login.txt') as file:
        loginInfo = json.load(file)

    return loginInfo

def pakTables(cursor):
    tablesLijst = []
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for i in tables:
        for j in i:
            tablesLijst.append(j)
    return tablesLijst

def tabelInformatie(tabel, db, cursor):
    print("Hoi")
    resultaat = {}

    cursor.execute("SELECT * FROM " + tabel)
    ophaal = cursor.fetchall()

    return ophaal

def regelMaker():
    prin("hoi")



    return regels

def voorstel(regels, informatie):
    pritn("hoi")
    for regel in regels:
        print(regel)


def testCase():
    loginInfo = autoLogin()
    db, cursor = mysqlConnectie(loginInfo)
    tabLijst = pakTables(cursor)
    test = tabelInformatie("brand", db, cursor)
    test2 = tabelInformatie("gender", db, cursor)
    print(test)
    print(test2)

    print(tabLijst)
    mysqlSluit(db, cursor)

testCase()

