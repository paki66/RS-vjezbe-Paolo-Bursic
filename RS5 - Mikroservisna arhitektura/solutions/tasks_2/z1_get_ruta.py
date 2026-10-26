"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u JSON formatu.
Svaki proizvod je rječnik koji sadrži ključeve naziv, cijena i količina. Pošaljite zahtjev na adresu http://localhost:8081/proizvodi
koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
"""

from aiohttp import web

app = web.Application()

async def get_products(request):
    products = [
        {
            "naziv": "mlijeko",
            "cijena": 1.5,
            "kolicina": 12
        },
        {
            "naziv": "kruh",
            "cijena": 1.5,
            "kolicina": 3
        }
    ]
    return web.json_response(products)

app.router.add_get("/proizvodi", get_products)

web.run_app(app, host="localhost", port=8081)