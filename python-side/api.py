from typing import Optional
from fastapi import FastAPI, Request, Response, Cookie
from fastapi.responses import JSONResponse
import json

app = FastAPI()


@app.get("/ok")
def home():
    return Response(
        status_code=200,
        content=json.dumps("Identity API Active"),
    )


@app.post("/create")
async def home(req: Request, res: Response):
    data = await req.json()
    res.set_cookie(
        key="fakesession",
        value="fake-cookie-session-value",
        httponly=True,
        samesite="strict",
    )
    return data


@app.post("/create2")
async def create_cookie(req: Request):
    data = await req.json()
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="session", value=data, httponly=True)
    return response


@app.post("/getCookie")
async def get_cookie(ads_id: Optional[str] = Cookie(None)):
    print(ads_id)
    return "love is magical"
