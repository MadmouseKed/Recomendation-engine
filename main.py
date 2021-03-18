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
    Voor eenvoud wordt de loginInfo in 1 lijst; [], meegegeven via loginInfo
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

def leesColumns(cursor, tabelNaam):
    tablesLijst = []
    cursor.execute("SHOW COLUMNS FROM " +tabelNaam)
    info = cursor.fetchall()
    resultaat = []
    for item in info:
        resultaat.append(item[0])
    return resultaat

def tabelInformatie(tabel, cursor):
    cursor.execute("SELECT * FROM " + tabel)
    ophaal = cursor.fetchall()

    return ophaal

def regelMaker(cursor):
    regel = []


    return regel

def regelMakerUI(cursor):
    flag = True
    while flag:
        regelmakerUIInformatie()
        check = True
        while check:
            invoer = input()
            print(invoer)
            print(type(invoer))
            if invoer == '1':
                print(pakTables(cursor))
                check = False
            elif invoer == '2':
                print(2)
                check = False
            elif invoer == '3':
                regelMaker(cursor)
                check = False
            elif invoer == '4':
                flag = False
                check = False
            else:
                print('Geen geldige input')

def voorstelVerwerking(regel, data, columns, cursor):
    """"
    Hulpstuk voor voorstel(), verwerkt elke individuele regel naar wens.
    """
    resultaat = []
    i = 0
    columnID = ""
    while i < len(columns) - 1:
        if regel[0] in columns[i]:
            columnID = i
            break
        i += 1

    idLijst = []
    keyLijst = tabelInformatie(regel[0], cursor)

    for set in keyLijst:
        if set[-1] in regel:
            idLijst.append(set[0])

    for product in data:
        if product[columnID] in idLijst:
            resultaat.append(product)

    return resultaat

def voorstel(regels, informatieTabel, cursor):
    """"
    Leest de regels uit en haalt de data waarover deze regels gaan besluiten op uit de informatieTabel,
    vervolgens schrijft het een lijst van items die voldoen aan de regels.
    :param regels bestaat uit een lijst van individuele regels. Elke regel wordt in volgorde van de lijst toegepast,
    alleen items die aan alle regels voldoen blijven over in het einde.
    :param informatieTabel
    :param cursor
    """
    data = tabelInformatie(informatieTabel, cursor)
    columns = leesColumns(cursor, informatieTabel)

    for regel in regels:
        data = voorstelVerwerking(regel, data, columns, cursor)
    return data

def retrieve_tabel_data(table, cursor):
    """
    Maak een dictionary aan en execute een querry voor het opvragen van alle data in het table.
    voor elke item in de lijst voeg de key en value toe aan een dictionary
    :param table:
    :param db:
    :return:
    """
    # divine a dictonary
    result_dict = {}

    # retrieve all items from selected table
    cursor.execute("SELECT * FROM " + table)
    myresult = cursor.fetchall()

    # for each item in myresult
    for item in myresult:
        result_dict[item[1]] = item[0]
    return result_dict

def testCase(testcase):
    loginInfo = autoLogin()
    db, cursor = mysqlConnectie(loginInfo)

    # tabLijst = pakTables(cursor)
    # print(leesColumns(cursor, "GENDER"))
    # test = tabelInformatie("brand", cursor)
    # # test2 = tabelInformatie("gender", cursor)
    # print(test)
    # print(test2)
    # regelMaker(cursor)
    # voorstel(testcase, "products", cursor)

    # a = "brand"
    # b = "brand_id_key"
    # if a in b:
    #     print("True")
    # else:
    #     print("False")

    # peanut = retrieve_tabel_data("products", cursor)
    # print(peanut)
    # print(peanut["Maya"])
    # products = tabelInformatie("products", cursor)
    # print(products[0])
    # print(type(products[0]))
    a = voorstel(testcase ,"products" ,cursor)
    print(a)
    # column = leesColumns(cursor, "products")
    # print(column)


    mysqlSluit(db, cursor)
    # show

testcase = [["brand", "Maya", "Famosa", "Familie Pos"]]

testCase(testcase)