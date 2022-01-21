from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse
from starlette.responses import JSONResponse
import mysql.connector, requests, json

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	auth_plugin='mysql_native_password',
)
print(db)

mycursor = db.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)


# async def app(request):
#    return JSONResponse({"re":"vfv"})

async def homepage(request):
    apiresp = requests.get("https://934f3f71-0be5-4ebc-8ce7-3f72ae4bddb6.mock.pstmn.io/resume/1")
    api = apiresp.json()
    print(api)
    return JSONResponse({'hello':'world'})

# async def nextpage(request):
#     return PlainTextResponse("Hello")

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    # Route('/hello', nextpage),
    # Route('/h', app),
])

