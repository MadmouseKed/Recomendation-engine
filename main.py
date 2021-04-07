""""
Test bestand voor het aanmaken van alle verbindingen.
(Nog) geen diepe UI integratie.
"""
from data_out import *
from Recomendations import *
import time

def main():
    """"
    Open verbinding met DB.

    """
    loginInfo = autoLogin()
    db, cursor = mysqlConnectie(loginInfo)
    start = time.time()
    """"
    Content filtering
    Drop de table als deze al bestaat voor testen.
    Maak een tabel
    """
    cursor.execute(dropTable("Opdracht3"))

    """Aanmaken van tabel voor voorstel."""
    voorstelTabel = createTable("Opdracht3","id","filter","product1","product2","product3","product4")
    cursor.execute(voorstelTabel)

    contentFiltering(db,cursor, 0)
    """"
    Collaberative filtering
    """
    print(collaborativeFiltering(db,cursor, 10))
    """"
    Sluit verbinding met DB.

    """
    end = time.time()
    print(f"Done: {end - start}")
    mysqlSluit(db, cursor)

main()