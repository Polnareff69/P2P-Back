# Services/university_service.py

import uuid
from Config.db import conn
from Models.university import University
from Repositories.GenericRepository import GenericRepository
from Schemas.university import UniversityCreate, UniversityUpdate

university_repo = GenericRepository(session=conn, model=University)


class UniversityService:

    def create_university(data: UniversityCreate):
        new_university = University(
            id=uuid.uuid4(),
            name=data.name,
            address=data.address
        )
        return university_repo.create(new_university)

    def get_university_by_id(university_id: uuid.UUID):
        university = university_repo.get_by_id("id", university_id)
        if not university:
            raise ValueError(f"No se encontró la universidad con ID: {university_id}")
        return university

    def get_all_universities():
        return university_repo.get_all()

    def update_university(university_id: uuid.UUID, data: UniversityUpdate):
        updated = university_repo.update("id", university_id, data.dict(exclude_unset=True))
        return updated

    def delete_university(university_id: uuid.UUID):
        deleted = university_repo.delete("id", university_id)
        return deleted
