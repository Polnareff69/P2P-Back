# services/auction_service.py

import uuid
from config.db import conn
from models.auction import Auction
from models.users import User
from models.products import Product
from repositories.generic_repository import GenericRepository
from schemas.auctions import AuctionCreate, AuctionUpdate

# Instancias de repositorios
auction_repo = GenericRepository(session=conn, model=Auction)
user_repo = GenericRepository(session=conn, model=User)
product_repo = GenericRepository(session=conn, model=Product)


class AuctionService:

    @staticmethod
    def create_auction(auction: AuctionCreate):
        """
        Crea una nueva subasta después de validar que el usuario y el producto existen.
        """
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

    @staticmethod
    def get_auction_by_id(auction_id: uuid.UUID):
        """
        Obtiene una subasta por su ID, incluyendo las relaciones de propietario y producto.
        """
        auction = auction_repo.get_by_id_relation("id", auction_id, relationships=["owner", "product"])
        if not auction:
            raise ValueError(f"No se encontró la subasta con ID: {auction_id}")
        return auction

    @staticmethod
    def get_all_auctions():
        """
        Obtiene todas las subastas disponibles.
        """
        return auction_repo.get_all()

    @staticmethod
    def update_auction(auction_id: uuid.UUID, auction_data: AuctionUpdate):
        """
        Actualiza los datos de una subasta existente.
        """
        updated = auction_repo.update("id", auction_id, auction_data.dict(exclude_unset=True))
        return updated

    @staticmethod
    def delete_auction(auction_id: uuid.UUID):
        """
        Elimina una subasta por su ID.
        """
        deleted = auction_repo.delete("id", auction_id)
        return deleted
