from aiohttp import web

async def check_facts(request):
    data = await request.json()
    filtered_facts = []
    for fact in data['facts']:
        if fact.find('cat') != -1:
            filtered_facts.append(fact)
    return web.json_response({"facts": filtered_facts}, status=200)

app = web.Application()
app.router.add_patch('/facts', check_facts)

web.run_app(app, host='localhost', port=8087)