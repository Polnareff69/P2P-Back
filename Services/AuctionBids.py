# Services/auction_bid_service.py

import uuid
from Config.db import conn
from Models.auction_bids import AuctionBid
from Models.auction import Auction
from Models.users import User
from Repositories.GenericRepository import GenericRepository
from Schemas.auction_bids import AuctionBidCreate

auction_bid_repo = GenericRepository(session=conn, model=AuctionBid)
auction_repo = GenericRepository(session=conn, model=Auction)
user_repo = GenericRepository(session=conn, model=User)


class AuctionBidService:

    def createBid(bid: AuctionBidCreate):
        auction = auction_repo.get_by_id("id", bid.auction_id)
        user = user_repo.get_by_id("UserId", bid.user_id)

        if not auction or not user:
            raise ValueError("Subasta o usuario no encontrado")

        new_bid = AuctionBid(
            id=uuid.uuid4(),
            auction_id=bid.auction_id,
            user_id=bid.user_id,
            bid_amount=bid.bid_amount
        )
        return auction_bid_repo.create(new_bid)

    def getBidById(bid_id: uuid.UUID):
        return auction_bid_repo.get_by_id_relation("id", bid_id, relationships=["auction", "user"])

    def getAllBids():
        return auction_bid_repo.get_all_with_relations(["user"])


    def deleteBid(bid_id: uuid.UUID):
        return auction_bid_repo.delete("id", bid_id)
