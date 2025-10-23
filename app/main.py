from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/programming")
def programming(request: Request):
    cards = [
        {"title": "ООП", "img": "/static/images/oop.jpg"},
        {"title": "WEB-программирование", "img": "/static/images/web.jpg"},
    ]
    return templates.TemplateResponse("programming.html", {"request": request, "cards": cards})

@app.get("/design")
def design(request: Request):
    cards = [
        {"title": "Базы данных", "img": "/static/images/db.jpg"},
        {"title": "UML", "img": "/static/images/uml.jpg"},
    ]
    return templates.TemplateResponse("design.html", {"request": request, "cards": cards})

@app.get("/ai")
def ai(request: Request):
    cards = [
        {"title": "Машинное обучение", "img": "/static/images/ai.jpg"},
        {"title": "Нейросети", "img": "/static/images/ai.jpg"},
    ]
    return templates.TemplateResponse("ai.html", {"request": request, "cards": cards})

@app.get("/dev")
def dev(request: Request):
    cards = [
        {"title": "АИС", "img": "/static/images/ais.jpg"},
        {"title": "Сайты", "img": "/static/images/site.jpg"},
    ]
    return templates.TemplateResponse("dev.html", {"request": request, "cards": cards})
