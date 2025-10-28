from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# === Подключаем статику и шаблоны ===
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

news_center = {
    "global": [
        {
            "title": "Добавлены новые направления MetaCode",
            "date": "01.06.2025",
            "scope": "Платформа",
        },
        {
            "title": "Обновлён шаблон административной панели",
            "date": "28.05.2025",
            "scope": "Платформа",
        },
        {
            "title": "Расширена программа по искусственному интеллекту",
            "date": "18.05.2025",
            "scope": "Платформа",
        },
    ],
    "sections": {
        "programming": [
            {
                "title": "В раздел добавлен курс по TypeScript",
                "date": "27.05.2025",
                "scope": "Раздел «Программирование»",
            },
            {
                "title": "Опубликован план по Python-проектам",
                "date": "19.05.2025",
                "scope": "Раздел «Программирование»",
            },
        ],
        "design": [
            {
                "title": "Обновлены шаблоны диаграмм UML",
                "date": "25.05.2025",
                "scope": "Раздел «Проектирование»",
            }
        ],
        "ai": [
            {
                "title": "Добавлен черновик курса по генеративным моделям",
                "date": "29.05.2025",
                "scope": "Раздел «ИИ»",
            }
        ],
        "dev": [
            {
                "title": "Появился план по корпоративным АИС",
                "date": "22.05.2025",
                "scope": "Раздел «Разработка»",
            }
        ],
    },
    "subsections": {
        "web": [
            {
                "title": "Определение мобильного устройства в JavaScript",
                "date": "25.05.2025",
                "scope": "Подраздел «Web-разработка»",
            },
            {
                "title": "Загрузка данных с сервера в D3.js",
                "date": "30.03.2025",
                "scope": "Подраздел «Web-разработка»",
            },
        ]
    },
    "courses": {
        "javascript": [
            {
                "title": "Чек-лист подготовки уроков по DOM",
                "date": "24.05.2025",
                "scope": "Курс «Руководство по JavaScript»",
            },
            {
                "title": "Обновлены задания по модулю «Переменные»",
                "date": "15.05.2025",
                "scope": "Курс «Руководство по JavaScript»",
            },
        ]
    },
}

# === Главная структура сайта ===
site_sections = {
    "programming": {
        "title": "Программирование",
        "cards": [
            {"title": "ООП", "img": "/static/images/oop.jpg", "key": "oop"},
            {"title": "Web", "img": "/static/images/web.jpg", "key": "web"},
            {"title": "Python", "img": "/static/images/python.jpg", "key": "python"},
        ],
        "news": news_center["sections"].get("programming", news_center["global"]),
    },
    "design": {
        "title": "Проектирование",
        "cards": [
            {"title": "Базы данных", "img": "/static/images/db.jpg", "key": "db"},
            {"title": "UML диаграммы", "img": "/static/images/uml.jpg", "key": "uml"},
        ],
        "news": news_center["sections"].get("design", news_center["global"]),
    },
    "ai": {
        "title": "Искусственный интеллект",
        "cards": [
            {"title": "Машинное обучение", "img": "/static/images/ai.jpg", "key": "ml"},
            {"title": "Нейросети", "img": "/static/images/nn.jpg", "key": "nn"},
        ],
        "news": news_center["sections"].get("ai", news_center["global"]),
    },
    "dev": {
        "title": "Разработка",
        "cards": [
            {"title": "Сайты", "img": "/static/images/site.jpg", "key": "sites"},
            {"title": "АИС", "img": "/static/images/ais.jpg", "key": "ais"},
        ],
        "news": news_center["sections"].get("dev", news_center["global"]),
    },
}

# === Подразделы ===
subsections = {
    "web": {
        "title": "Web-разработка",
        "description": "Раздел посвящён HTML, CSS, JS, Node.js, React, Vue и современному фронтенду.",
        "topics": ["HTML5/CSS3", "JavaScript", "Node.js", "React", "Vue 3", "Angular"],
        "news": news_center["subsections"].get("web", news_center["global"]),
    },
}

# === Курсы ===
courses = {
    "javascript": {
        "title": "Руководство по JavaScript",
        "description": "JavaScript — язык, добавляющий интерактивность и динамику веб-страницам.",
        "news": news_center["courses"].get("javascript", news_center["global"]),
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
@@ -91,107 +178,319 @@ console.log("Привет, мир!");
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


admin_summary = [
    {
        "label": "Главных разделов",
        "value": len(site_sections),
        "note": "в навигации верхнего уровня",
    },
    {
        "label": "Подразделов",
        "value": len(subsections),
        "note": "готовы к наполнению контентом",
    },
    {"label": "Активных курсов", "value": 6, "note": "в разработке и публикации"},
    {
        "label": "Аккаунтов админов",
        "value": 3,
        "note": "ведут авторство, модерацию и редактуру",
    },
]

admin_menu_items = [
    {
        "id": "programming",
        "title": "Программирование",
        "icon": "<>",
        "order": 1,
        "published": True,
        "subsections": 3,
    },
    {
        "id": "design",
        "title": "Проектирование",
        "icon": "⚙",
        "order": 2,
        "published": True,
        "subsections": 2,
    },
    {
        "id": "ai",
        "title": "Искусственный интеллект",
        "icon": "🧠",
        "order": 3,
        "published": False,
        "subsections": 4,
    },
    {
        "id": "dev",
        "title": "Разработка",
        "icon": "💻",
        "order": 4,
        "published": True,
        "subsections": 1,
    },
]

admin_subsections = [
    {
        "id": "web",
        "title": "Web-разработка",
        "parent": "Программирование",
        "courses": 3,
        "status": "На модерации",
        "status_class": "status-pending",
        "updated": "2 часа назад",
    },
    {
        "id": "databases",
        "title": "Базы данных",
        "parent": "Проектирование",
        "courses": 2,
        "status": "Опубликован",
        "status_class": "status-published",
        "updated": "Вчера",
    },
    {
        "id": "ml",
        "title": "Машинное обучение",
        "parent": "Искусственный интеллект",
        "courses": 4,
        "status": "Черновик",
        "status_class": "status-draft",
        "updated": "5 часов назад",
    },
]

admin_courses = [
    {
        "title": "Руководство по JavaScript",
        "subsection": "Web-разработка",
        "lessons": 24,
        "progress": 70,
        "status": "Черновик",
        "status_class": "status-draft",
    },
    {
        "title": "Основы TypeScript",
        "subsection": "Web-разработка",
        "lessons": 12,
        "progress": 40,
        "status": "На модерации",
        "status_class": "status-pending",
    },
    {
        "title": "Проектирование REST API",
        "subsection": "Базы данных",
        "lessons": 9,
        "progress": 100,
        "status": "Опубликован",
        "status_class": "status-published",
    },
    {
        "title": "Введение в нейросети",
        "subsection": "Машинное обучение",
        "lessons": 18,
        "progress": 55,
        "status": "Черновик",
        "status_class": "status-draft",
    },
]

admin_activity = [
    {"author": "MetaCode Admin", "action": "обновил меню «Программирование»", "when": "15 мин назад"},
    {"author": "Мария Лебедева", "action": "создала подраздел «UX-практика»", "when": "1 час назад"},
    {"author": "Виктор Смирнов", "action": "отправил курс «ML продвинутый» на модерацию", "when": "Сегодня"},
    {"author": "MetaCode Admin", "action": "заблокировал пользователя @spam-alert", "when": "Вчера"},
]

admin_roadmap = [
    {"title": "Интеграция с CRM", "note": "синхронизация обращений и лидов"},
    {"title": "Роли и права", "note": "гибкая матрица доступа для команды"},
    {"title": "Импорт программ", "note": "загрузка курсов из CSV и Google Sheets"},
]

admin_users = [
    {
        "username": "@meta-admin",
        "name": "MetaCode Admin",
        "role": "Администратор (главный)",
        "status": "Активен",
        "status_class": "status-published",
        "courses": 12,
        "registered": "12.03.2023",
    },
    {
        "username": "@content-admin",
        "name": "Мария Лебедева",
        "role": "Администратор (редактор контента)",
        "status": "Активен",
        "status_class": "status-published",
        "courses": 7,
        "registered": "22.08.2023",
    },
    {
        "username": "@moderator-admin",
        "name": "Виктор Смирнов",
        "role": "Администратор (модератор)",
        "status": "Активен",
        "status_class": "status-published",
        "courses": 4,
        "registered": "05.01.2024",
    },
]

admin_news = [
    {
        "title": "Добавлен курс «Руководство по JavaScript»",
        "scope": "Раздел «Программирование»",
        "status": "Опубликовано",
        "status_class": "status-published",
        "date": "01.06.2025",
    },
    {
        "title": "Создан подраздел «UX-практика»",
        "scope": "Раздел «Проектирование»",
        "status": "Черновик",
        "status_class": "status-draft",
        "date": "28.05.2025",
    },
    {
        "title": "Подготовлен анонс по генеративному ИИ",
        "scope": "Раздел «ИИ»",
        "status": "На модерации",
        "status_class": "status-pending",
        "date": "26.05.2025",
    },
]

# === Главная страница ===
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "news": news_center["global"]},
    )


# === Раздел ===
@app.get("/section/{name}", response_class=HTMLResponse)
async def section(request: Request, name: str):
    section = site_sections.get(name)
    if not section:
        return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

    return templates.TemplateResponse("section.html", {
        "request": request,
        "mode": "cards",
        "section_title": section["title"],
        "cards": section["cards"],
        "news": section.get("news", news_center["global"]),
    })


# === Подраздел ===
@app.get("/subsection/{subname}", response_class=HTMLResponse)
async def subsection(request: Request, subname: str, topic: Optional[str] = None):
    sub = subsections.get(subname)
    if not sub:
        return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

    if topic:
        course_key = topic.lower()
        course = courses.get(course_key)
        if not course:
            return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

        return templates.TemplateResponse("section.html", {
            "request": request,
            "mode": "course",
            "section_title": course["title"],
            "course_key": course_key,
            "description": course["description"],
            "chapters": course["chapters"],
            "news": course.get("news", news_center["subsections"].get(subname, news_center["global"])),
        })

    return templates.TemplateResponse("section.html", {
        "request": request,
        "mode": "content",
        "section_title": sub["title"],
        "description": sub["description"],
        "topics": sub["topics"],
        "news": sub.get("news", news_center["global"]),
        "sub_slug": subname,
    })


# === Урок ===
@app.get("/lesson/{course_key}/{chapter_index}/{lesson_index}", response_class=HTMLResponse)
async def lesson_page(request: Request, course_key: str, chapter_index: int, lesson_index: int):
    course_data = courses.get(course_key)
    if not course_data:
        return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

    if not (0 <= chapter_index < len(course_data["chapters"])):
        return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

    chapter = course_data["chapters"][chapter_index]
    if not (0 <= lesson_index < len(chapter["lessons"])):
        return templates.TemplateResponse("index.html", {"request": request, "news": news_center["global"]})

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
        "news": course_data.get("news", news_center["global"]),
    })


# === Административная панель ===
@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "summary": admin_summary,
            "menu_items": admin_menu_items,
            "subsections": admin_subsections,
            "courses": admin_courses,
            "activity": admin_activity,
            "roadmap": admin_roadmap,
            "users": admin_users,
            "news_items": admin_news,
        },
    )