main
testcase bestand, roept de functies aan om de tabellen aan te maken en om de tabellen vervolgens in te vullen.

data_out
Handelt het communiceren van het programma naar de database.

db_query
handelt het communiceren van de database naar het programma.

Recomendations
Handelt de data verwerkng logica voor het aanmaken of ophalen van voorstellen.

	content Filtering
	werkt op basis van de sub_category key
	1. Haal informatie van het profiel op
	2. Bepaal de meest voorkoomende sub_category key van het profiel
	3. Haal alle producten op met dezelfde sub_category key
	4. Neem van deze producten 4 random producten als voorstel.
	5. Schrijf het voorstel weg samen met de profielID en de sub_category (als filter) key.

	collaborative Filtering
	werkt op basis van de sb_category key
	1. Haal informatie van het profiel op
	2. Bepaal de meest voorkomende sub_Category key van het profiel.
	3. Haal alle voorstellen op van profielen die dezelfde sub_category key als filter hebben.
	4. Kies 1 voorstel uit en print deze