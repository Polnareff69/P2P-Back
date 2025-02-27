# Repositories/GenericRepository.py
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import as_declarative

class GenericRepository:
    def __init__(self, session: Session, model):
        self.session = session  # La sesión de SQLAlchemy
        self.model = model      # El modelo que este repositorio gestionará
    
    def create(self, data):
        """Crear una nueva entidad."""
        instance = self.model(**data)
        self.session.add(instance)
        self.session.commit()
        return instance
    
    def get_by_id(self, entity_id):
        """Obtener una entidad por su ID."""
        return self.session.query(self.model).filter_by(id=entity_id).first()
    
    def get_all(self):
        """Obtener todas las entidades de ese modelo."""
        return self.session.query(self.model).all()
    
    def update(self, entity_id, data):
        """Actualizar una entidad existente."""
        entity = self.get_by_id(entity_id)
        if entity:
            for key, value in data.items():
                setattr(entity, key, value)
            self.session.commit()
            return entity
        return None
    
    def delete(self, entity_id):
        """Eliminar una entidad por su ID."""
        entity = self.get_by_id(entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return entity
        return None
