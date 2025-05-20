# Routers/auction.py

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from Schemas.auctions import AuctionCreate, AuctionUpdate, AuctionOut, AuctionFullOut
from Services.Auctions import AuctionService
from Utils.Auth import verify_token

auction = APIRouter(tags=["Subastas"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auction.post('/auction', response_model=AuctionOut)
def create_auction(data: AuctionCreate, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        auction = AuctionService.createAuction(data, token)
        return AuctionOut.model_validate(auction)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@auction.get('/auction/{auction_id}', response_model=AuctionFullOut)
def get_auction_by_id(auction_id: UUID):
    auction = AuctionService.getAuctionById(auction_id)
    if not auction:
        raise HTTPException(status_code=404, detail="Auction not found")
    return AuctionFullOut.model_validate(auction)


@auction.get('/auctions', response_model=list[AuctionOut])
def get_all_auctions():
    return AuctionService.getAllAuctions()


@auction.put('/auction/{auction_id}', response_model=AuctionOut)
def update_auction(auction_id: UUID, data: AuctionUpdate):
    updated = AuctionService.updateAuction(auction_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Auction not found")
    return AuctionOut.model_validate(updated)


@auction.delete('/auction/{auction_id}')
def delete_auction(auction_id: UUID):
    result = AuctionService.deleteAuction(auction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found")
    return JSONResponse(status_code=200, content={"message": "Auction deleted successfully"})
