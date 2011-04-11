# Procedura sciagniecia danych:
1. W skrypty/downloader.py ustawiamy adres naszej bazy danych.
2. Sciagamy http://www.jitonomic.com/Api/MarketProducts/xml
3. Instalujemy [couchdb-python](http://code.google.com/p/couchdb-python)
4. Odpalamy skrypt podajac mu sciezke do sciagnietego pliku xml
5. czekamy..

# MapReduce
Widoki zawierajace podaz i popyt pogrupowane po kategorii, grupie, produkcie.

> couchapp push widoki.js http://sigma.inf.ug.edu.pl:14016/marketproduct

Lub odpowiednik napisany w pythonie ( wymaga [couchdb-python](http://code.google.com/p/couchdb-python) )

> ./widoki.py

# Wizualizacja
Wizualizcja widoku zawierającego dane dotyczące podazy.
Wymagana jest biblioteka [couchquery](http://mikeal.github.com/couchquery)
Tworzymy lokalne pliki z danymi:
> ./prepareTree.py

> ./prepareForce.py

I otwieramy pliki html w przeglądarce.
Wizualizacja przeprowadzona z użyciem biblioteki JavaScriptu [protovis](http://vis.stanford.edu/protovis)
Gotowe wizualizacje
 * [force](http://piwnica.gotdns.org/~dogrizz/wizualizacja/force.html)
 * [circle tree](http://piwnica.gotdns.org/~dogrizz/wizualizacja/tree.html) trzeba poszukac danych na wykresie (jest ogromny)
 * [dendogram](http://piwnica.gotdns.org/~dogrizz/wizualizacja/dendogram.html)