from db_query import *
import random
"""
main_category recomendations.
"""
def orderProfielen(cursor):
    """
    haalt alle profielen op met daarin hun order geschiedenis. (geen duplicates)
    :param cursor: cursor key
    :return: data: profielen met hun order geschiedenis.
    """
    query = selectTable(["sessions.profiles_id_key"], ["orders", "sessions"], ["sessions.id", "orders.sessions_id_key"])
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def getProfileContent(cursor,profileid,select,van,waar):
    """
    Haalt de inhoud van een profiel op op basis van de voorwarden, select, van en waar.
    :param cursor: cursor key.
    :param profileid: id van het profiel
    :param select: wat we gaan selecteren
    :param van: uit welke tabel we selecteren
    :param waar: welke verbanden we selecteren
    :return: data: de infromatie die aan alle voorwaarden voldoet.
    """
    item = "'" + str(profileid) + "'"
    query = selectTable(select,van,waar)
    # print(f"Query: {query}")
    cursor.execute(query)
    data = cursor.fetchall()
    return data

# def getCategory():
"""
content filtering
"""
def contentFiltering(db,cursor, aantal):
    """
    content filtering op basis van aankopen klant.
    De code bepaalt de klant zijn meest populaire sub categorie,op basis daarvan stelt de code 4 producten voor met dezelfde sub categorie.
    :param db: db key
    :param cursor: cursor key
    :param aantal: Hoeveel profielen er gedaan worden. als aantal = 0 dan alle profielen.
    """
    isNull = True
    teller = 0
    if aantal == 0:
        isNull = False

    profielen = orderProfielen(cursor)
    for profiel in profielen:
        if isNull:
            if teller == aantal:
                break
            teller += 1
        teller += 1
        productIDS = []
        producten = {}
        profielString = "'" + str(profiel[0]) + "'"
        profielInfo = getProfileContent(cursor, profiel,["products.id", "orders.aantal", "sub_category.sub_category", "orders.sessions_id_key", "sessions.profiles_id_key"],
                                        ["products", "sub_category", "orders", "sessions"], ["products.sub_category_id_key", "sub_category.id", "orders.products_id_key", "products.id",
                                                           "orders.sessions_id_key", "sessions.id", "profiles_id_key", profielString])
        for set in profielInfo:
            if set[2] not in producten:
                producten[set[2]] = 1
            elif set[2] in producten:
                producten[set[2]] += 1

        producten = sorted(producten, key=producten.get, reverse=True)[:1]

        productItem = '"' + str(producten[0]) + '"'

        query = selectTable(["products.id", "products.sub_category_id_key"], ["products", "sub_category"],
                        ["products.sub_category_id_key", "sub_category.id", "sub_category.sub_category", productItem])

        cursor.execute(query)
        subCategoryProducten = cursor.fetchall()

        for itemID, subCategoryID in (subCategoryProducten):
             productIDS.append(itemID)

        try:
            voortelItems = random.sample(productIDS, 4)
        except:
            voortelItems = []

            for product in productIDS:
                voortelItems.append(product)

            while len(voortelItems) < 4:
                voortelItems.append("None")

        voorstel = [profiel[0]] + [producten[0]] + voortelItems
        
        query = insertQuerry("Opdracht3","id","filter","product1","product2","product3","product4")

        cursor.execute(query, voorstel)
        db.commit()

""""
collaborative filtering
"""
def collaborativeFiltering(db,cursor, aantal):
    """
    content filtering op basis van andere gebruikers.
    De code bekijkt welke sub categorie deze gebruiker het meest gebruikt, en op basis daarvan haalt de code
    een voorstel op van een profiel met dezelfde subcategorie.
    :param db:
    :param cursor:
    :param aantal:
    """
    isNull = True
    teller = 0
    if aantal == 0:
        isNull = False

    profielen = orderProfielen(cursor)

    for profiel in profielen:
        if isNull:
            if teller == aantal:
                break
            teller += 1

        producten = {}
        profielString = "'" + str(profiel[0]) + "'"

        profielInfo = getProfileContent(cursor, profiel, ["products.id", "orders.aantal", "sub_category.sub_category",
                                                          "orders.sessions_id_key", "sessions.profiles_id_key"],
                                        ["products", "sub_category", "orders", "sessions"],
                                        ["products.sub_category_id_key", "sub_category.id", "orders.products_id_key",
                                         "products.id",
                                         "orders.sessions_id_key", "sessions.id", "profiles_id_key", profielString])

        for set in profielInfo:
            if set[2] not in producten:
                producten[set[2]] = 1
            elif set[2] in producten:
                producten[set[2]] += 1
        producten = sorted(producten, key=producten.get, reverse=True)[:1]

        filterID = '"' + str(producten[0]) + '"'
        query = selectTable(["id","product1","product2","product3","product4"], ["Opdracht3"],
                            ["Opdracht3.filter", filterID])
        cursor.execute(query)
        vergelijkProfielen = cursor.fetchall()
        # print(query)
        # print(f"{vergelijkProfielen}")
        pick = random.sample(vergelijkProfielen, 1)[0]
        resultaat = (f"Voor profiel {profiel[0]} vergelijken we het met profiel: {pick[0]} \n"
              f"Met de producten {pick[1]} {pick[2]} {pick[3]} {pick[4]}")
        print(resultaat)