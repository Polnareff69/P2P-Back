# Repositories/GenericRepository.py
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import joinedload


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
    
    def get_by_id(self, name_field ,entity_id):
        """Obtener una entidad por su ID."""
        return self.session.query(self.model).filter(getattr(self.model, name_field) == entity_id).first()
    
    def get_all(self):
        """Obtener todas las entidades de ese modelo."""
        return self.session.query(self.model).all()
    
    # repositories/GenericRepository.py
    def update(self, name_field ,entity_id, data: dict):
        """Actualizar una entidad existente de manera dinámica, pero ignorando valores null/None."""
        entity = self.get_by_id(name_field, entity_id)
        
        if entity:
            for key, value in data.items():
                if value is None:  # Si el valor es None (equivalente a null en JSON), lo ignoramos.
                    continue
                if hasattr(entity, key):
                    setattr(entity, key, value)
                else:
                    print(f"Atributo {key} no existe en la entidad {self.model.__name__}")
            
            self.session.commit()
            return entity
        return None

    
    def delete(self, name_field ,entity_id):
        """Eliminar una entidad por su ID."""
        entity = self.get_by_id(name_field, entity_id)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return entity
        return None
    
    def get_by_name(self, name_field: str, name_value: str):
        """Obtener una entidad por su nombre."""
        return self.session.query(self.model).filter(getattr(self.model, name_field) == name_value).first()


    def updateByName(self, ColumnName, CompaniName, data: dict):
        """Actualizar una entidad existente de manera dinámica, pero ignorando valores null/None."""
        entity = self.get_by_name(ColumnName , CompaniName)
        
        if entity:
            for key, value in data.items():
                if value is None:  # Si el valor es None (equivalente a null en JSON), lo ignoramos.
                    continue
                if hasattr(entity, key):
                    setattr(entity, key, value)
                else:
                    print(f"Atributo {key} no existe en la entidad {self.model.__name__}")
            
            self.session.commit()
            return entity
        return None
    
 

    def get_by_id_relation(self, name_field ,entity_id, relationships: list = []):
        query = self.session.query(self.model)

        for rel in relationships:
            query = query.options(joinedload(getattr(self.model, rel)))

        return query.filter(getattr(self.model, name_field) == entity_id).first()
