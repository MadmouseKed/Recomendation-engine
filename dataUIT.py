import mysql.connector

gebruiker = "root"
wachtwoord = ""
dbNaam = "test"
host = "localhost"

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
    cursor.execute(
        "CREATE TABLE " + tabelNaam + " (id VARCHAR(255) PRIMARY KEY UNIQUE, price INTEGER(10), stock INTEGER(10), flavor VARCHAR(255) NULL, kleur VARCHAR(255) NULL, recomendable BIT(10), fast_mover BIT(10), gender_id_key INTEGER(10), doelgroep_id_key INTEGER(10), brand_id_key INTEGER(10), main_category_id_key INTEGER(10), sub_category_id_key INTEGER(10), FOREIGN KEY(gender_id_key) REFERENCES gender(id), FOREIGN KEY(brand_id_key) REFERENCES brand(id), FOREIGN KEY(main_category_id_key) REFERENCES main_category(id), FOREIGN KEY(doelgroep_id_key) REFERENCES doelgroep(id), FOREIGN KEY(sub_category_id_key) REFERENCES sub_category(id))")
    insertWaarden(tabelInfo, db, cursor, tabelNaam, "id", "price", "stock", "flavor", "kleur", "recomendable", "fast_mover", "gender_id_key", "doelgroep_id_key", "brand_id_key", "main_category_id_key", "sub_category_id_key")

# def mysqlTableInformatie():
