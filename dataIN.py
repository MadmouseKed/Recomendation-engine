import mysql.connector

#connectie naar mySQL
# def mysqlConnectie(gebruiker, wachtwoord, dbNaam, host):
#     """"
#     Verbinding met de gekozen mysql database.
#     :arg gebruiker ; Gebruikersnaam
#     :arg wachtwoord ; wachtwoord behorend bij gebruikersnaam
#     :arg dbNaam ; de naam van de database waarin gezoekt moet worden.
#     :arg host ; de link naar de server. Voor localhost gebruik ("localhost")
#     """
#     db = mysql.connector.connect(host=host, user=gebruiker, password=wachtwoord, database=dbNaam)
#     cursor = db.cursor()
#
#     return db, cursor

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