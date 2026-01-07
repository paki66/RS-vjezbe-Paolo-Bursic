"""
Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći get_cat_fact korutinu
koja šalje GET zahtjev na URL: https://catfact.ninja/fact. Izradite 20 Task objekata za dohvaćanje činjenica o mačkama
te ih pozovite unutar main korutine i rezultate pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina
filter_cat_facts ne šalje HTTP zahtjeve, već zaprima gotovu listu činjenica (stringova) o mačkama i vraća novu listu
koja sadrži samo one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

Primjer konačnog ispisa:

Filtrirane činjenice o mačkama:
- A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.
- The first cat in space was a French cat named Felicette (a.k.a. “Astrocat”) In 1963, France blasted the cat into outer space. Electrodes implanted in her brains sent neurological signals back to Earth. She survived the trip.
- The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1 pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm) long.
- The first commercially cloned pet was a cat named "Little Nicky." He cost his owner $50,000, making him one of the most expensive cats ever.
- In the 1750s, Europeans introduced cats into the Americas to control pests.
- A group of cats is called a clowder.
"""

