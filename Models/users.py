from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String
from Config.db import meta, engine
import uuid
from sqlalchemy.dialects.postgresql import UUID


users = Table("users", meta, 
              Column("UserId",UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
              Column("Name", String(255)),
              Column("Email", String(255)),
              Column("Password", String(255))
              )
meta.create_all(engine)