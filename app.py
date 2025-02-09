from fastapi import FastAPI
from Routes.users import user

app = FastAPI()
app.include_router(user)

