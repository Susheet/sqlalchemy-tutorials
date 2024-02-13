from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.orm import (Mapped, declarative_base, mapped_column,
                            relationship, sessionmaker)

db_url = "sqlite:///ep_06_user_address_database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(ForeignKey("users.id"))


class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Address)


Base.metadata.create_all(engine)
session = Session()

# Creating users
user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)

# Creating addresses
address1 = Address(street="123 Main St", city="New York", state="NY", zip_code="10001")
address2 = Address(street="456 Oak Ave", city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(street="789 Pine Rd", city="Chicago", state="IL", zip_code="60601")

# Associating addresses with users
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

# Adding users and addresses to the session and committing changes to the database
session.add(user1)
session.add(user2)
session.commit()


print(f'address1: {address1.user = }')
print(f"user1:    {user1.addresses = }")
print(f"user2:    {user2.addresses = }")