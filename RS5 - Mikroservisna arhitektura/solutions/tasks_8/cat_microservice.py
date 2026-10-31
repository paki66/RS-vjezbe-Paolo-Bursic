import aiohttp
from aiohttp import web

async def get_cat_facts(request):
    amount = int(request.match_info.get('amount'))
    facts = []
    async with aiohttp.ClientSession() as session:
        while amount > 0:
            data = await session.get("https://catfact.ninja/fact")
            response = await data.json()
            facts.append(response['fact'])
            amount -= 1
    return web.json_response({"facts": facts}, status=200)

app = web.Application()
app.router.add_get("/cat/{amount}", get_cat_facts)

web.run_app(app, host='localhost', port=8086)