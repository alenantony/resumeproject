# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.post("/items")
# def read_item(item_id: dict, q: Optional[str] = None):
#     print(item_id)
#     return {"item_id": item_id, "q": q}

# =============================
# =============================

# from starlette.applications import Starlette
# from starlette.routing import Route
# from starlette.responses import JSONResponse
# import requests
# from starlette.responses import PlainTextResponse, HTMLResponse
# import json
# # from starlette.testclient import TestClient
# # from starlette.testclient import TestClient
# # from starlette.websockets import WebSocket

# async def homepage(request):
#     response = request.get("http://127.0.0.1:8000/items")
#     print("==",response)
#     # print("world")
#     # response = response.json()
#     # return PlainTextResponse("Yes")
#     return PlainTextResponse("hello")

# async def returnpage(request):
#     # print("ok")
#     response = request.get("/yes")
#     return PlainTextResponse("++++++++++++++++")


# app = Starlette(debug=True, routes=[
#     Route('/', homepage),
#     Route('/items', homepage, methods=["POST"]),
#     Route('/yes', returnpage)
# ])

# =============================
# =============================


# from starlette.applications import Starlette
# from starlette.responses import JSONResponse
# from starlette.routing import Route
# import requests
# import json

# async def homepage(request):
#     # r = requests.get('127.0.0.1:8000/hello', data = {'key':'value'})
#     # data = requests.get('127.0.0.1:8000/hello')
#     # print(data)
#     response = request.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
#     print(response.json())
#     return JSONResponse({'hello': 'world'})

# routes = [
#     Route("/hello", endpoint=homepage)
# ]

# app = Starlette(debug=True, routes=routes)

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/items")
async def read_item(item: dict, q: Optional[str] = None):
    print(item)
    return {"item_id": item, "q": q}