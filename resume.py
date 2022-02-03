from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
import json
from validation import Resume

async def insert_values(request):
    resume_data = [await request.json()]
    # print(resume_data)
    try:
        print(resume_data[0])
        response = [Resume(**p) for p in resume_data]
        print("============================1",response[0][0])
        exit
    except:
        return JSONResponse({"Value":"Error"})
    print("============================1")
    # print(resume_data)
    return JSONResponse({"HELLO":"WORLD"})
    # print(resume_data)
    # except ValidationError as ver:
    #     print("Value error")
    # # print(resume_data)
    # # print(validation)
    # return JSONResponse({"Hello":"World"})

routes = [
    Route("/build", endpoint=insert_values, methods = ["POST"])
]

app = Starlette(
    routes = routes
)