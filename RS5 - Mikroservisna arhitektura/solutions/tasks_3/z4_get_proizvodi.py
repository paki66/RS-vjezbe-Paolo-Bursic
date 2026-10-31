"""
Definirajte aiohttp poslužitelj koji radi na portu 8081. Poslužitelj mora imati dvije rute: /proizvodi i /proizvodi/{id}.
Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod prema ID-u.
Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne postoji'}.

Proizvode pohranite u listu rječnika:

Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.
"""
from aiohttp import web, ClientSession
import asyncio

proizvodi = [
  {"id": 1, "naziv": "Laptop", "cijena": 5000},
  {"id": 2, "naziv": "Miš", "cijena": 100},
  {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
  {"id": 4, "naziv": "Monitor", "cijena": 1000},
  {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_products(request):
    return web.json_response(proizvodi)

async def get_product(request):
    product_id = request.match_info.get("id")
    print(product_id)
    for product in proizvodi:
        if product["id"] == int(product_id):
            return web.json_response(product, status=200)
    return web.json_response({'error': 'No such product'}, status=404)


async def process_messages():
    async with ClientSession() as session:
        products = await session.get('http://localhost:8080/proizvodi')
        products_dict = await products.json()
        print(products_dict)

        product_2 = await session.get('http://localhost:8080/proizvodi/2')
        product_2_dict = await product_2.json()
        print(product_2_dict)


async def start_server():
    app = web.Application()
    app.router.add_get("/proizvodi/{id}", get_product)
    app.router.add_get("/proizvodi", get_products)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")


async def main():
    asyncio.create_task(process_messages())
    asyncio.create_task(start_server())
    await asyncio.Event().wait()

asyncio.run(main())