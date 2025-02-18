from fastapi import FastAPI
from Routes.users import user
from Routes.Auth import router as auth_router

app = FastAPI()
app.include_router(user)
app.include_router(auth_router)
