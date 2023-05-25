from fastapi import FastAPI

from routers import users, electronics

app = FastAPI()

app.include_router(
    users.router,
    prefix='/api/users',
    tags=['users'],
)
app.include_router(
    electronics.router,
    prefix='/api/electronics',
    tags=['electronics'],
)
