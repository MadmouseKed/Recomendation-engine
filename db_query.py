""""
Hulp formule's voor het ophalen van informatie uit de DB.
"""

def insertQuerry(tabelnaam, *column):
    """
    Deze functie maakt een querry aan, op basis van tabelnaam en column(s).
    :param tabelnaam: Naam van de tabel waar in geinsert moet worden.
    :param column: column namen van de tabel.
    :return:
    """
    query = "INSERT IGNORE INTO " + tabelnaam
    qColumn = " (" + column[0]
    values = " VALUES (%s"
    i = 1
    while i < len(column):
        qColumn += ", " + column[i]
        values += ", %s"
        i += 1
    query += qColumn + ")" + values + ")"
    return query

def selectTable(selectList, fromlist, where):
    """
    maakt een select querry aan, alle items in een tabel worden gekozen
    :param selectList: form [tabelnaam.columnnaam] meerdere opties kunnen gekozen worden door ze allemaal in een lijst te zetten.
    :param fromlist: form [tabelnaam] meerder opties kunnen gekozen worden door ze allemaal in een lijst te zetten.
    :param where: form [tabelnaam.columnnaam, tabelnaam.columnnaam] setjes van twee stukken informatie die je wilt vergelijken.
    :return: query die de gewenste data in de juiste combinatie ophaalt.
    """
    query = "SELECT "

    for item in range(len(selectList) - 1):
        query += str(selectList[item]) + ", "
    query += selectList[-1] + " "

    query += "FROM "

    for item in range(len(fromlist) - 1):
        query += str(fromlist[item]) + ", "
    query += fromlist[-1] + " "

    query += "WHERE "

    count = 0
    while count != len(where):
        query += str(where[count]) + " = " + str(where[count + 1])
        count += 2
        if count != len(where):
            query += " AND "

    return query