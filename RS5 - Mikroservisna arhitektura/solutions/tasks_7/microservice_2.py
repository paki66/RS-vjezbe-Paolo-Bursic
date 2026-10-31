from aiohttp import web

async def pomnozi(request):
    body = await request.json()
    filtered_list = [s for s in body if type(s) is int]
    if len(filtered_list) == 0:
        return web.json_response(text="List does not contain numbers", status=400)
    result = 1
    for num in filtered_list:
        result *= num
    return web.json_response(result, status=200)

app = web.Application()
app.router.add_post("/umnozak", pomnozi)

web.run_app(app, host='localhost', port=8084)