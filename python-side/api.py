from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response, Cookie, Depends
from fastapi.responses import JSONResponse
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
import json
import datetime

expiring_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
    minutes=5
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    # allow_credentials=True,
    allow_methods=["*"],  # include additional methods as per the application demand
    allow_headers=["*"],  # include additional headers as per the application demand
)


class CsrfSettings:
    secret_key: str = "Kaakaww!"


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}

# app = FastAPI()


@app.get("/ok")
def home():
    return Response(
        status_code=200,
        content=json.dumps("Identity API Active"),
    )


# @app.post("/create")
# async def home(req: Request, res: Response, token: str = Depends(oauth2_scheme)):
#     data = await req.json()
#     res.set_cookie(
#         key="fakesession",
#         value="fake-cookie-session-value",
#         httponly=True,
#         samesite="strict",
#     )
#     return data


@app.post("/create")
async def home(req: Request, res: Response, csrf_protect: CsrfProtect = Depends()):
    data = await req.json()
    res.set_cookie(
        key="fakesession",
        value="fake-cookie-session-value",
        httponly=True,
        expires=expiring_date
        # samesite="strict",
    )
    return data


@app.post("/create2")
async def create_cookie(
    req: Request,
    session: Optional[str] = Cookie(default=None),
    csrf_protect: CsrfProtect = Depends(),
):
    data = await req.json()
    print(session)
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(status_code=200, content=content)
    response.set_cookie(key="session", value=data, httponly=True)
    csrf_protect.set_csrf_cookie(response)
    return response


@app.post("/getCookie")
async def get_cookie(
    session: Optional[str] = Cookie(default=None), csrf_protect: CsrfProtect = Depends()
):
    print(session)
    response = JSONResponse(status_code=200, content={"csrf_token": "cookie"})
    csrf_protect.set_csrf_cookie(response)
    return "love is magical"
