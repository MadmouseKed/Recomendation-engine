import mysql.connector

gebruiker = "root"
wachtwoord = ""
dbNaam = "test"
host = "localhost"

#connectie naar mySQL
def mysqlConnectie(gebruiker, wachtwoord, dbNaam, host):
    """"
    Verbinding met de gekozen mysql database.
    :arg gebruiker ; Gebruikersnaam
    :arg wachtwoord ; wachtwoord behorend bij gebruikersnaam
    :arg dbNaam ; de naam van de database waarin gezoekt moet worden.
    :arg host ; de link naar de server. Voor localhost gebruik ("localhost")
    """
    db = mysql.connector.connect(host=host, user=gebruiker, password=wachtwoord, database=dbNaam)
    cursor = db.cursor()

    return db, cursor

def mysqlSluit(db, cursor):
    cursor.close()
    db.commit()
    db.close()

# def mysqlTableInformatie():
