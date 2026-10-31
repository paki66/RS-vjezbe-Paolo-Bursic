from aiohttp import web

async def zbroji(request):
    body = await request.json()
    filtered_list = [s for s in body if type(s) is int]
    if len(filtered_list) == 0:
        return web.json_response(text="List does not contain numbers", status=400)
    return web.json_response(sum(filtered_list))

app = web.Application()
app.router.add_post('/zbroj', zbroji)

web.run_app(app, host='localhost', port=8083)