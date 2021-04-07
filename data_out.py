import mysql.connector
import json

def createTable(tabelnaam, *column):
    """
    maakt query aan die tabel aanmaakt in DB
    :param tabelnaam: naam van de tabel
    :param column: namen van de columns die in de tabel moeten komen.
    :return: query voor het aanmaken van de tabel.
    """
    values = " VARCHAR(255)"
    query = "CREATE TABLE IF NOT EXISTS " + tabelnaam + "(" + column[0] + values + " PRIMARY KEY UNIQUE"
    i = 1
    while i < len(column):
        query += ", " + column[i] + values + " NULL"

        i += 1
    query += ")"
    return query

def dropTable(tabelNaam):
    """
    maakt query aan voor het droppen van de tabelNaam tabel
    :param tabelNaam: naam van de te droppen tabel
    :return: query voor het droppen van de tabel. Als deze bestaat.
    """
    query = "DROP TABLE IF EXISTS " + tabelNaam
    return query

def autoLogin():
    """
    Probeert inlogin informatie te vinden in login.txt, als deze niet gevonden wordt moet de gebruiker eenmalig
    de informatie invoeren.
    :return: loginDict, een dictionary waarin alle login gegevens staan voor mysqlConnectie
    """
    loginDict = {}
    # banner()
    try:
        open('login.txt')
    except FileNotFoundError:
        loginDict['host'] = input("\n\t" + "Geef je host op: ", "yellow")
        loginDict['gebruiker'] = input("\n\t" + "Geef je mysql username op: ", "yellow")
        loginDict['wachtwoord'] = input("\n\t" + "Geef je mysql password op: ", "yellow")
        loginDict["dbNaam"] = input("\n\t" + "Geef je mysql database op: ", "yellow")
        with open('login.txt', 'w') as file:
            file.write(json.dumps(loginDict))
            file.close()

    with open('login.txt') as file:
        loginDict = json.load(file)
    return loginDict

def mysqlConnectie(loginInfo):
    """"
    Verbinding met de gekozen mysql database.
    Voor eenvoud wordt de loginInfo in 1 lijst; [], meegegeven via loginInfo
    :param loginInfo: dictaat met alle informatie die er nodig is om in te loggen.
    :arg gebruiker ; Gebruikersnaam
    :arg wachtwoord ; wachtwoord behorend bij gebruikersnaam
    :arg dbNaam ; de naam van de database waarin gezoekt moet worden.
    :arg host ; de link naar de server. Voor localhost gebruik ("localhost")
    """
    db = mysql.connector.connect(host=loginInfo["host"], user=loginInfo["gebruiker"], password=loginInfo["wachtwoord"], database=loginInfo["dbNaam"])
    cursor = db.cursor()

    return db, cursor

def mysqlSluit(db, cursor):
    """
    sluit de verbinding met de mysql database, en commit de laatste items die nog in de wachtrij staan.
    :param db: database key
    :param cursor: cursor key
    """
    cursor.close()
    db.commit()
    db.close()
