from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.database import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.coin.router import router as router_coin
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html

from src.comment.router import router as router_comment


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui.min.css")


applications.get_swagger_ui_html = swagger_monkey_patch


app = FastAPI(
    title="FastAPI",
    description="Fastapi Interface Document",
    version="2.0.0",
)

app.include_router(router_coin)
app.include_router(router_comment)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym"


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
