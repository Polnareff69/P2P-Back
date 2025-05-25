from fastapi import FastAPI
from Routes.Companies import company
from Routes.users import user
from Routes.Auth import router as auth_router
from Routes.Products import product
from Routes.Auctions import auction
from Routes.AuctionBid import bid
from Routes.University import university

app = FastAPI()
app.include_router(user)
app.include_router(auth_router)
app.include_router(product)
app.include_router(company)
app.include_router(auction)
app.include_router(bid)
app.include_router(university)