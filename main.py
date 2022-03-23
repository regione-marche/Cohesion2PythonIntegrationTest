from fastapi import FastAPI, Request

from CohesionIntegration.cohesion import Cohesion

app = FastAPI()
cohesion = Cohesion()

@app.get("/")
async def root():
    return {
            'login':"http://127.0.0.1:8000/login",
            'logout': "http://127.0.0.1:8000/logout"
            }


@app.get("/login")
async def login():
    cohesion.login()

    return "logging in..."


@app.post("/callback")
async def callback(request: Request):
    body = (await request.body()).decode("utf-8")
    prefix = 'auth='
    payload = body[body.startswith(prefix) and len(prefix):]
    result = cohesion.get_credential(payload)

    return result


@app.get("/logout")
async def logout(sso: str = "", aspnet_sso: str = ""):
    return "OK" if cohesion.logout(sso, aspnet_sso) == 200 else "KO"