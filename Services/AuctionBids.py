# services/auction_bid_service.py

import uuid
from config.db import conn
from models.auction_bids import AuctionBid
from models.auction import Auction
from models.users import User
from repositories.generic_repository import GenericRepository
from schemas.auction_bids import AuctionBidCreate

# Instancias de repositorios
auction_bid_repo = GenericRepository(session=conn, model=AuctionBid)
auction_repo = GenericRepository(session=conn, model=Auction)
user_repo = GenericRepository(session=conn, model=User)


class AuctionBidService:
    @staticmethod
    def create_bid(bid: AuctionBidCreate):
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

    @staticmethod
    def get_bid_by_id(bid_id: uuid.UUID):
        return auction_bid_repo.get_by_id_relation("id", bid_id, relationships=["auction", "user"])

    @staticmethod
    def get_all_bids():
        return auction_bid_repo.get_all()

    @staticmethod
    def delete_bid(bid_id: uuid.UUID):
        return auction_bid_repo.delete("id", bid_id)
