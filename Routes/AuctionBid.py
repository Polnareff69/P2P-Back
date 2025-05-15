# Routers/auction_bid.py

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from Schemas.auction_bids import AuctionBidCreate, AuctionBidOut, AuctionBidFullOut
from Services.AuctionBids import AuctionBidService
from Utils.Auth import verify_token

bid = APIRouter(tags=["Pujas"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@bid.post('/bid', response_model=AuctionBidOut)
def create_bid(data: AuctionBidCreate, token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        bid = AuctionBidService.createBid(data)
        return AuctionBidOut.model_validate(bid)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@bid.get('/bid/{bid_id}', response_model=AuctionBidFullOut)
def get_bid_by_id(bid_id: UUID):
    bid = AuctionBidService.getBidById(bid_id)
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    return AuctionBidFullOut.model_validate(bid)


@bid.get('/bids', response_model=list[AuctionBidOut])
def get_all_bids():
    return AuctionBidService.getAllBids()


@bid.delete('/bid/{bid_id}')
def delete_bid(bid_id: UUID):
    result = AuctionBidService.deleteBid(bid_id)
    if not result:
        raise HTTPException(status_code=404, detail="Bid not found")
    return JSONResponse(status_code=200, content={"message": "Bid deleted successfully"})
