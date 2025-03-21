from fastapi import FastAPI
from Routes.Companies import company
from Routes.Users import user
from Routes.Auth import router as auth_router
from Routes.Products import product

app = FastAPI()
app.include_router(user)
app.include_router(auth_router)
app.include_router(product)
app.include_router(company)
