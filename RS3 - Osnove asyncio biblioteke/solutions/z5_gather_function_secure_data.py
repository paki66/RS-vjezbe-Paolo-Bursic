"""
Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka.
Kako se u praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3 sekunde.
Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime, broj_kartice i CVV.
Definirajte listu s 3 rječnika osjetljivih podataka.
Pohranite u listu zadaci kao u prethodnom zadatku te pozovite zadatke koristeći asyncio.gather().
Korutina secure_data mora za svaki rječnik vratiti novi rječnik u obliku:
    {'prezime':prezime, 'broj_kartice': 'enkriptirano', 'CVV': 'enkriptirano'}.
Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash vrijednost ulaznog stringa.
"""