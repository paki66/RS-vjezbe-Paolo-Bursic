"""
Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API servisa.

Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts. Nakon toga, definirajte
korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na URL: https://catfact.ninja/fact.

Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
funkciju u listu dog_cat_facts, a zatim ih koristeći list slicing odvojite u dvije liste obzirom da znate da je prvih 5
činjenica o psima, a drugih 5 o mačkama (bez obzira što mrežni rezultati različito "dolaze", gather ih pohranjuje redoslijedom poziva).

Na kraju definirajte treću korutinu mix_facts koja prima dvije liste, dog_facts i cat_facts, te vraća novu listu u kojoj
se za svaki indeks i nalazi odabrana činjenica prema sljedećem pravilu: uzmite činjenicu o psima ako je njezina duljina
veća od duljine odgovarajuće mačje činjenice; u suprotnom odaberite mačju činjenicu. Za paralelnu iteraciju dviju lista
upotrijebite funkciju zip, npr. for dog_fact, cat_fact in zip(dog_facts, cat_facts). Nakon dobivanja nove liste,
ispišite filtrirani skup činjenica.

Primjer konačnog ispisa:

Mixane činjenice o psima i mačkama:

If they have ample water, cats can tolerate temperatures up to 133 °F.
Dogs with little human contact in the first three months typically don’t make good pets.
The most popular dog breed in Canada, U.S., and Great Britain is the Labrador retriever.
An estimated 1,000,000 dogs in the U.S. have been named as the primary beneficiaries in their owner’s will.
When a cats rubs up against you, the cat is marking you with it's scent claiming ownership.
"""