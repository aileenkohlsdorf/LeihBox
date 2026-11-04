from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="LeihBox API",
    description="Backend für die Geräteausleihe",
    version="1.0.0",
    docs_url=None
)

@app.get("/", tags=["Allgemein"])
def root():
    return {"message": "Willkommen bei LeihBox!"}

@app.get("/health", tags=["Allgemein"])
def health():
    return {"status": "ok"}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui():
    response = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI"
    )

    html = response.body.decode("utf-8")

    dark_css = """
    <style>
        body {
            background-color: #171717 !important;
            color: #eeeeee !important;
        }

        .swagger-ui {
            filter: invert(88%) hue-rotate(180deg);
        }

        .swagger-ui img,
        .swagger-ui svg {
            filter: invert(100%) hue-rotate(180deg);
        }
    </style>
    """

    html = html.replace("</head>", dark_css + "</head>")

    return HTMLResponse(content=html)
