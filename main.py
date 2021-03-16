import dataUIT
import dataIN
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

    print(ophaal)

def testCase():
    loginInfo = autoLogin()
    db, cursor = mysqlConnectie(loginInfo)
    tabLijst = pakTables(cursor)
    print(tabelInformatie("Brand", db, cursor))
    print(tabLijst)
    mysqlSluit(db, cursor)

testCase()

