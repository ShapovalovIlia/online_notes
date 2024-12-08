from sqlalchemy import Column, MetaData, Table, UUID, String, TIMESTAMP

metadata = MetaData()

user_table = Table(
    "users",
    metadata,
    Column("id", primary_key=True, type_=UUID, nullable=False),
    Column("login", type_=String, nullable=False),
    Column("password", type_=String, nullable=False),
    Column("name", type_=String, nullable=False),
    Column("surname", type_=String, nullable=True),
    Column("email", type_=String, nullable=True),
)

note_table = Table(
    "notes",
    metadata,
    Column("id", primary_key=True, type_=UUID, nullable=False),
    Column("tag", type_=String, nullable=False),
    Column("content", type_=String, nullable=False),
    Column("created_at", type_=TIMESTAMP, nullable=False),
    Column("updated_at", type_=TIMESTAMP, nullable=True),
)
