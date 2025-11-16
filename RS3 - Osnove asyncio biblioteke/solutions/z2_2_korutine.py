"""
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba.
Prva korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde,
a druga korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5 sekundi.
Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate.
Program se mora izvršavati ~5 sekundi.
"""