from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# === Подключаем статику и шаблоны ===
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# === Главная структура сайта ===
site_sections = {
    "programming": {
        "title": "Программирование",
        "cards": [
            {"title": "ООП", "img": "/static/images/oop.jpg", "key": "oop"},
            {"title": "Web", "img": "/static/images/web.jpg", "key": "web"},
            {"title": "Python", "img": "/static/images/python.jpg", "key": "python"},
        ],
    },
    "design": {
        "title": "Проектирование",
        "cards": [
            {"title": "Базы данных", "img": "/static/images/db.jpg", "key": "db"},
            {"title": "UML диаграммы", "img": "/static/images/uml.jpg", "key": "uml"},
        ],
    },
    "ai": {
        "title": "Искусственный интеллект",
        "cards": [
            {"title": "Машинное обучение", "img": "/static/images/ai.jpg", "key": "ml"},
            {"title": "Нейросети", "img": "/static/images/nn.jpg", "key": "nn"},
        ],
    },
    "dev": {
        "title": "Разработка",
        "cards": [
            {"title": "Сайты", "img": "/static/images/site.jpg", "key": "sites"},
            {"title": "АИС", "img": "/static/images/ais.jpg", "key": "ais"},
        ],
    },
}

# === Подразделы ===
subsections = {
    "web": {
        "title": "Web-разработка",
        "description": "Раздел посвящён HTML, CSS, JS, Node.js, React, Vue и современному фронтенду.",
        "topics": ["HTML5/CSS3", "JavaScript", "Node.js", "React", "Vue 3", "Angular"],
        "news": [
            {"title": "Определение мобильного устройства в JavaScript", "date": "25.05.2025"},
            {"title": "Загрузка данных с сервера в D3.js", "date": "30.03.2025"},
        ],
    },
}

# === Курсы ===
courses = {
    "javascript": {
        "title": "Руководство по JavaScript",
        "description": "JavaScript — язык, добавляющий интерактивность и динамику веб-страницам.",
        "chapters": [
            {
                "name": "Глава 1. Введение в JavaScript",
                "lessons": [
                    {
                        "title": "Что такое JS",
                        "content": """
<p>JavaScript — язык программирования, который делает веб-страницы интерактивными.</p>
<pre><code class="language-js">
// Пример кода
console.log("Привет, мир!");
</code></pre>
"""
                    },
                    {
                        "title": "Первая программа",
                        "content": """
<p>Создадим первую программу в браузере:</p>
<pre><code class="language-html">
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;meta charset="utf-8"&gt;&lt;/head&gt;
&lt;body&gt;
&lt;script&gt;
    console.log("Моя первая программа!");
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>
<p>Открой файл в браузере и посмотри результат в консоли.</p>
"""
                    },
                ],
            },
            {
                "name": "Глава 2. Основы JavaScript",
                "lessons": [
                    {
                        "title": "Переменные",
                        "content": """
<p>Переменные объявляются с помощью <code>let</code> или <code>const</code>:</p>
<pre><code class="language-js">
let name = "Иван";
const age = 25;
</code></pre>
"""
                    },
                ],
            },
        ],
    }
}

# === Главная страница ===
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# === Раздел ===
@app.get("/section/{name}")
async def section(request: Request, name: str):
    section = site_sections.get(name)
    if not section:
        return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse("section.html", {
        "request": request,
        "mode": "cards",
        "section_title": section["title"],
        "cards": section["cards"],
    })


# === Подраздел ===
@app.get("/subsection/{subname}")
async def subsection(request: Request, subname: str, topic: str | None = None):
    sub = subsections.get(subname)
    if not sub:
        return templates.TemplateResponse("index.html", {"request": request})

    if topic:
        course_key = topic.lower()
        course = courses.get(course_key)
        if not course:
            return templates.TemplateResponse("index.html", {"request": request})

        return templates.TemplateResponse("section.html", {
            "request": request,
            "mode": "course",
            "section_title": course["title"],
            "course_key": course_key,
            "description": course["description"],
            "chapters": course["chapters"],
            "news": sub["news"],
        })

    return templates.TemplateResponse("section.html", {
        "request": request,
        "mode": "content",
        "section_title": sub["title"],
        "description": sub["description"],
        "topics": sub["topics"],
        "news": sub["news"],
        "sub_slug": subname,
    })


# === Урок ===
@app.get("/lesson/{course_key}/{chapter_index}/{lesson_index}", response_class=HTMLResponse)
async def lesson_page(request: Request, course_key: str, chapter_index: int, lesson_index: int):
    course_data = courses.get(course_key)
    if not course_data:
        return templates.TemplateResponse("index.html", {"request": request})

    if not (0 <= chapter_index < len(course_data["chapters"])):
        return templates.TemplateResponse("index.html", {"request": request})

    chapter = course_data["chapters"][chapter_index]
    if not (0 <= lesson_index < len(chapter["lessons"])):
        return templates.TemplateResponse("index.html", {"request": request})

    lesson = chapter["lessons"][lesson_index]

    return templates.TemplateResponse("section.html", {
        "request": request,
        "mode": "lesson",
        "course_title": course_data["title"],
        "course_key": course_key,
        "chapter_title": chapter["name"],
        "lesson_title": lesson["title"],
        "lesson_content": lesson["content"],
        "chapters": course_data["chapters"],
        "current_chapter": chapter_index,
        "current_lesson": lesson_index,
    })
