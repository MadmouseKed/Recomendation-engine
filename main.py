from dataIN import *
from dataUIT import *
from consoleUI import *
import dataUIT
import json
import mysql

def mysqlSluit(db, cursor):
    cursor.close()
    db.commit()
    db.close()

# def mysqlCommit(tabelInfo, db, cursor, tabelNaam, *column):
#     cursor.execute("CREATE TABLE " + tabelNaam + " (id VARCHAR(255) PRIMARY KEY UNIQUE, price INTEGER(10), stock INTEGER(10), flavor VARCHAR(255) NULL, kleur VARCHAR(255) NULL, recomendable BIT(10), fast_mover BIT(10), gender_id_key INTEGER(10), doelgroep_id_key INTEGER(10), brand_id_key INTEGER(10), main_category_id_key INTEGER(10), sub_category_id_key INTEGER(10), FOREIGN KEY(gender_id_key) REFERENCES gender(id), FOREIGN KEY(brand_id_key) REFERENCES brand(id), FOREIGN KEY(main_category_id_key) REFERENCES main_category(id), FOREIGN KEY(doelgroep_id_key) REFERENCES doelgroep(id), FOREIGN KEY(sub_category_id_key) REFERENCES sub_category(id))")
#     insertWaarden(tabelInfo, db, cursor, tabelNaam, "id", "price", "stock", "flavor", "kleur", "recomendable", "fast_mover", "gender_id_key", "doelgroep_id_key", "brand_id_key", "main_category_id_key", "sub_category_id_key")

def insertWaarden(tabelInfo, db, cursor, tabel, *column):
    """"
    Plaatst de waarden in de nieuw aangemaakte tabel
    """

    category_list_sql = "INSERT IGNORE INTO " + tabel + " (" + column[0] + ", " + column[1] + ", " + column[2] + ", " + column[3] + ", " + column[4] + ", " + column[5] + ", " + column[6] + ", " + column[7] + ", " + column[8] + ", " + column[9] + ", " + column[10] + ", " + column[11] + ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for list1 in tabelInfo:
        category_list_sql_value = (list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7], list1[8], list1[9], list1[10], (list1[11]))
        cursor.execute(category_list_sql, category_list_sql_value)
    db.commit()

def mysqlCommit(tabelInfo, db, cursor, tabelNaam):
    cursor.execute("CREATE TABLE " + tabelNaam + " (id VARCHAR(255) PRIMARY KEY UNIQUE, price INTEGER(10), stock INTEGER(10), flavor VARCHAR(255) NULL, kleur VARCHAR(255) NULL, recomendable BIT(10), fast_mover BIT(10), gender_id_key INTEGER(10), doelgroep_id_key INTEGER(10), brand_id_key INTEGER(10), main_category_id_key INTEGER(10), sub_category_id_key INTEGER(10), FOREIGN KEY(gender_id_key) REFERENCES gender(id), FOREIGN KEY(brand_id_key) REFERENCES brand(id), FOREIGN KEY(main_category_id_key) REFERENCES main_category(id), FOREIGN KEY(doelgroep_id_key) REFERENCES doelgroep(id), FOREIGN KEY(sub_category_id_key) REFERENCES sub_category(id))")
    insertWaarden(tabelInfo, db, cursor, tabelNaam, "id", "price", "stock", "flavor", "kleur", "recomendable", "fast_mover", "gender_id_key", "doelgroep_id_key", "brand_id_key", "main_category_id_key", "sub_category_id_key")

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
    print(tabel)
    cursor.execute("SELECT * FROM " + tabel)
    ophaal = cursor.fetchall()

    return ophaal

def regelMaker(cursor, db):
    regel = []
    execute = regelMakerUI(cursor, db)

    return regel

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

    # testMenu()
    # testcase = [["brand", "Maya", "Famosa", "Familie Pos"]]
    a = voorstel(testcase, "products", cursor)
    tabelInfo = a
    tabelNaam = "testTabel1"
    print(a)
    mysqlCommit(tabelInfo, db, cursor, tabelNaam)


    mysqlSluit(db, cursor)
    # show
#
# testcase = [["brand", "Maya", "Famosa", "Familie Pos"]]
testcase = [["brand", "Maya", "Famosa", "Familie Pos"],["doelgroep", "Kinderen"]]
testCase(testcase)

# testMenu()