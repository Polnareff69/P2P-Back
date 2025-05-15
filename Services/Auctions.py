# Services/auction_service.py

import uuid
from Config.db import conn
from Models.auction import Auction
from Models.users import User
from Models.products import Product
from Repositories.GenericRepository import GenericRepository
from Schemas.auctions import AuctionCreate, AuctionUpdate

auction_repo = GenericRepository(session=conn, model=Auction)
user_repo = GenericRepository(session=conn, model=User)
product_repo = GenericRepository(session=conn, model=Product)


class AuctionService:
    
    def createAuction(auction: AuctionCreate):
        # Validamos que existan las entidades referenciadas
        user = user_repo.get_by_id("UserId", auction.owner_id)
        product = product_repo.get_by_id("productid", auction.product_id)

        if not user or not product:
            raise ValueError("Usuario o producto no encontrado")

        new_auction = Auction(
            id=uuid.uuid4(),
            product_id=auction.product_id,
            owner_id=auction.owner_id,
            start_date=auction.start_date,
            end_date=auction.end_date,
            initial_price=auction.initial_price,
            current_price=auction.current_price
        )
        return auction_repo.create(new_auction)

    def getAuctionById(auction_id: uuid.UUID):
        auction = auction_repo.get_by_id_relation("id", auction_id, relationships=["owner", "product"])
        if not auction:
            raise ValueError(f"No se encontró la subasta con ID: {auction_id}")
        return auction

    def getAllAuctions():
        return auction_repo.get_all()

    def updateAuction(auction_id: uuid.UUID, auction_data: AuctionUpdate):
        updated = auction_repo.update("id", auction_id, auction_data.dict(exclude_unset=True))
        return updated

    def deleteAuction(auction_id: uuid.UUID):
        deleted = auction_repo.delete("id", auction_id)
        return deleted
