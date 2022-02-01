from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
import json
from validation import Resume

async def insert_values(request):
    resume_data = [await request.json()]
    validation = [Resume(**p) for p in resume_data]
    print(resume_data)
    print(validation)
    return JSONResponse({"Hello":"World"})

routes = [
    Route("/build", endpoint=insert_values, methods = ["POST"])
]

app = Starlette(
    routes = routes
)