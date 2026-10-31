from aiohttp import web

async def divide(request):
    body = await request.json()
    if body["sum"] == 0:
        return web.json_response({"error": "division wih 0 not possible"}, status=400)
    result = body["umnozak"] / body['sum']
    return web.json_response(result, status=200)

app = web.Application()
app.router.add_post("/kolicnik", divide)

web.run_app(app, host='localhost', port=8085)