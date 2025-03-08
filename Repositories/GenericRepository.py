# Repositories/GenericRepository.py
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import as_declarative

class GenericRepository:
    def __init__(self, session: Session, model):
        self.session = session  
        self.model = model     
    
    def create(self, data):
        """Crear una nueva entidad."""
        if isinstance(data, self.model):
            # If data is an instance of the model, we need to create an instance based on the attributes.
            instance = data
        elif isinstance(data, dict):
            # If data is a dictionary, unpack it to create a new instance.
            instance = self.model(**data)
        else:
            raise TypeError(f"Expected data to be either a dictionary or an instance of {self.model.__name__}, but got {type(data)}")

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
    
    def get_by_name(self, name_field: str, name_value: str):
        """Obtener una entidad por su nombre."""
        return self.session.query(self.model).filter(getattr(self.model, name_field) == name_value).first()
