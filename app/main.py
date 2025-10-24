from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Все разделы и карточки
site_sections = {
    "programming": {
        "title": "Программирование",
        "cards": [
            {"title": "ООП", "img": "/static/images/oop.jpg"},
            {"title": "Web", "img": "/static/images/web.jpg"},
            {"title": "Python", "img": "/static/images/python.jpg"},
        ],
    },
    "design": {
        "title": "Проектирование",
        "cards": [
            {"title": "Базы данных", "img": "/static/images/db.jpg"},
            {"title": "UML диаграммы", "img": "/static/images/uml.jpg"},
        ],
    },
    "ai": {
        "title": "Искусственный интеллект",
        "cards": [
            {"title": "Машинное обучение", "img": "/static/images/ai.jpg"},
            {"title": "Нейросети", "img": "/static/images/nn.jpg"},
        ],
    },
    "dev": {
        "title": "Разработка",
        "cards": [
            {"title": "Сайты", "img": "/static/images/site.jpg"},
            {"title": "АИС", "img": "/static/images/ais.jpg"},
        ],
    },
}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/section/{name}")
async def section(request: Request, name: str):
    section = site_sections.get(name)
    if not section:
        return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse(
        "section.html",
        {"request": request, "section_title": section["title"], "cards": section["cards"]},
    )
