from fastapi import FastAPI
from Routes.users import user
from Routes.Auth import router as auth_router
from Routes.Products import product

app = FastAPI()
app.include_router(user)
app.include_router(auth_router)
app.include_router(product)
